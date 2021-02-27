# -*- coding: utf-8 -*-
import gzip
import os
import urllib
import urllib.parse
import urllib.error
from collections import Counter
import mitmproxy
from mitmproxy import http
from mitmproxy import ctx
import base64
import json
import jsonpath
from garbevents.settings import Settings as ST
from datetime import datetime

events_num = []


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
        :project=production                       生产环境上报埋点
        :project=default                          测试环境上报埋点
        :sa？gif？project=default&data=XXXXXXXX    app webview里面H5的JS上报埋点
        :sa？project=default                       app原生页面的上报埋点
        :sa.gif？project=default                   H5的JS上报埋点
        """
        # 引入时间搓

        global data_list
        now_time = datetime.now()
        new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')

        request_data = flow.request
        self.request_url = request_data.url
        api = self.request_url.split('/')[3]
        if ST.url in self.request_url:
            if 'default' in self.request_url:
                try:
                    # 解密格式# sa?project = default
                    api = self.request_url.split('/')[3]
                    request_content = str(flow.request.content).split('&')[2].split('=')[1]
                    gzip_data = urllib.parse.unquote(request_content)
                    data_list = json.loads(self.gzip_decompress(base64.b64decode(gzip_data)).decode('utf8'))

                except IndexError:
                    try:
                        # 解密格式sa.gif?project = default
                        request_content = str(flow.request.content).split('&')[0].split('=')[1]
                        # request_content = str(flow.request.content).split('&')[1].split('=')[1]
                        gzip_data = urllib.parse.unquote(request_content)
                        data_list = [json.loads(base64.b64decode(gzip_data).decode('utf8', errors='ignore'))]
                    except IndexError:
                        # 解密格式sa.gif?project = default&data=XXXXXXXX
                        request_content = str(self.request_url).split('&')[1].split('=')[1]
                        gzip_data = urllib.parse.unquote(request_content)
                        data_list = [json.loads(base64.b64decode(gzip_data).decode('utf8', errors='ignore'))]
                finally:
                    for result_list in data_list:
                        try:
                            event = result_list["event"]
                            count = Counter(events_num)
                            if event in ST.all_events:
                                events_num.append(event)
                                count = Counter(events_num)
                                ctx.log.info('累计的埋点事件统计次数{}'.format(count))
                                with open('{}/【H5和APP】累计的埋点事件统计次数.txt'.format(ST.report_path), 'w',
                                          encoding='utf-8') as file03:
                                    # 用于记录埋点事件参数没有值的统计.txt
                                    file03.write("【H5和APP】累计统计到的埋点次数{}!!!".format(count) + '\n')
                                ctx.log.info("获取到的埋点事件名称是 ====>{}".format(event))
                                # ctx.log.(result_list)
                                self.events_list.append(event)
                                # 用于遍历对应event事件里面的具体信息
                                for event_value in ST.events_properties[event]:
                                    # 记录下坑，下面不能直接在里面传event_value不然取不到值
                                    result = jsonpath.jsonpath(result_list, f"$..{event_value}")
                                    if result is False:
                                        ctx.log.info("请注意！！！请注意！！！{}事件未获取到{}值".format(event, event_value))
                                        with open('{}/【H5和APP】埋点事件参数没有值的统计.txt'.format(ST.report_path), 'a+',
                                                  encoding='utf-8') as file:
                                            # 用于记录埋点事件参数没有值的统计.txt
                                            file.write("{}请注意！！！请注意！！！{}事件未获取到{}值!!!".format(new_time, event,
                                                                                             event_value) + '\n')
                                    else:
                                        ctx.log.info("获取到的埋点事件:{}的自定义参数{}的值是{}：".format(event, event_value, result))

                                event_list = list(set(self.events_list))

                                if not os.path.exists(ST.report_path):
                                    os.mkdir(ST.report_path)
                                    ctx.log.info(ST.report_path + 'Successfully created！')

                                # 在已上报的埋点事件统计.txt记录已经获取到的事件
                                file = open('{}/【H5和APP】已上报的埋点事件统计.txt'.format(ST.report_path), 'w', encoding='utf-8')
                                for line in event_list:
                                    file.write(line + '\n')

                                # 通过记录到的事件和全部事件对比，在漏上报的埋点事件.txt记录漏上报的埋点事件
                                lost_list = list(set(ST.all_events).difference(set(event_list)))

                                if not lost_list:
                                    pass
                                else:
                                    ctx.log.info('暂未获取到这些埋点事件，可能存在漏上报事件 ====>{}'.format(lost_list))
                                    with open('{}/【H5和APP】漏上报的埋点事件统计.txt'.format(ST.report_path), 'w',
                                              encoding='utf-8') as file:
                                        for lines in lost_list:
                                            file.write(lines + '\n')
                            else:
                                pass
                        except KeyError:
                            ctx.log.warn("未获取需要的event事件 ====>可以忽略！")