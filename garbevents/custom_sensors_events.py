# -*- coding: utf-8 -*-
import gzip
import os
import urllib
import urllib.parse
import urllib.error
from pprint import pprint

from collections import Counter
import mitmproxy
from mitmproxy import http
from mitmproxy import ctx
import base64
import json
import jsonpath
from garbevents.settings import Settings as ST
from datetime import datetime, timedelta
from garbevents.logger import MyLogging

list2 = []
loging = MyLogging()


class GetData:
    """
    Personal customized version of 爱问医生
    A engine HTTP request class.
    """
    events_list = []
    now_time = datetime.now()
    new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def chunks(arr, n):
        """

        :param arr:
        :param n:
        :return:
        """
        return [arr[i:i + n] for i in range(0, len(arr), n)]

    @staticmethod
    def gzip_decompress(data):
        """
        解密上报数据
        :param data:
        :return:
        """
        try:
            return gzip.decompress(data)
        except AttributeError:
            from io import StringIO

            buf = StringIO()
            buf.write(data)
            fd = gzip.GzipFile(fileobj=buf, mode="r")
            fd.rewind()
            value = fd.read()
            fd.close()
            return value

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
        代理服务数据分析
        :param flow:
        :return:
        """
        # 引入时间搓
        now_time = datetime.now()
        new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')

        request_data = flow.request
        self.request_url = request_data.url

        # count = 0
        if ST.url in self.request_url:
            api = self.request_url.split('?')[0].split('/')[3]
            request_content = str(self.request_url).split('&')[1].split('=')[1]

            # 解密神策加密
            gzip_data = urllib.parse.unquote(request_content)
            data_list = [json.loads(base64.b64decode(gzip_data).decode('utf8', errors='ignore'))]

            for result_list in data_list:
                try:
                    event = result_list["event"]
                    count = Counter(list2)
                    if event in ST.all_events:
                        loging.info('累计的埋点事件统计次数{}'.format(count))
                        list2.append(event)
                        loging.info("获取到的埋点事件名称是 ====>{}".format(event))
                        # loging.(result_list)
                        self.events_list.append(event)
                        # 用于存放对应event事件里面的具体自定义埋点
                        eventdict = {}
                        # 用于遍历对应event事件里面的具体信息
                        for event_value in ST.events_properties[event]:
                            # 记录下坑，下面不能直接在里面传event_value不然取不到值
                            result = jsonpath.jsonpath(result_list, f"$..{event_value}")
                            if not result:
                                loging.info("请注意！！！请注意！！！{}事件未获取到{}值".format(event, event_value))
                                with open('{}/埋点事件参数没有值的统计.txt'.format(ST.report_path), 'a+', encoding='utf-8') as file:
                                    # 用于记录埋点事件参数没有值的统计.txt
                                    file.write(
                                        "{}请注意！！！请注意！！！{}事件未获取到{}值!!!".format(new_time, event, event_value) + '\n')
                            else:
                                loging.info("获取到的埋点事件:{}的自定义参数{}的值是{}：".format(event, event_value, result))
                    else:
                        pass
                except KeyError:
                    ctx.log.warn("未获取需要的event事件 ====>可以忽略！")

                event_list = list(set(self.events_list))

                if not os.path.exists(ST.report_path):
                    os.mkdir(ST.report_path)
                    ctx.log.info(ST.report_path + 'Successfully created！')

                # 在已上报的埋点事件统计.txt记录已经获取到的事件
                file = open('{}/已上报的埋点事件统计.txt'.format(ST.report_path), 'w', encoding='utf-8')
                for line in event_list:
                    file.write(line + '\n')

                # 通过记录到的事件和全部事件对比，在漏上报的埋点事件.txt记录漏上报的埋点事件
                lost_list = list(set(ST.all_events).difference(set(event_list)))
                file = open('{}/漏上报的埋点事件统计.txt'.format(ST.report_path), 'w', encoding='utf-8')
                for lines in lost_list:
                    loging.info('暂未获取到这些埋点事件，可能存在漏上报事件 ====>{}'.format(lines))
                    file.write(lines + '\n')
