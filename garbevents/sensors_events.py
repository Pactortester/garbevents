# -*- coding: utf-8 -*-
import gzip
import os
import urllib
import urllib.parse
import urllib.error
import mitmproxy
from mitmproxy import http
from mitmproxy import ctx
import base64
import json
from garbevents.settings import Settings as ST


class GetData:
    """
    A garbevents HTTP request class.
    """
    events_list = []

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

        :param flow:
        :return:
        """

        request_data = flow.request
        self.request_url = request_data.url

        if ST.url in self.request_url:

            ctx.log.info("url:-------->{}".format(self.request_url))
            api = self.request_url.split('/')[3]
            ctx.log.error("拆分后获取API地址====>{}".format(api))

            request_content = str(flow.request.content).split('&')[2].split('=')[1]
            ctx.log.info("拆分后获取加密数据====>{}".format(request_content))

            if request_content.find('%') == 0:
                gzip_data = urllib.parse.unquote(request_content)
                data = json.loads(self.gzip_decompress(base64.b64decode(gzip_data)).decode('utf8'))
                data_list = [data]
            else:
                data_list = json.loads(self.gzip_decompress(base64.b64decode(request_content)).decode('utf8'))

            for result_list in data_list:

                try:
                    event = result_list["event"]
                    ctx.log.error("解密数据后获取事件名====>{}".format(event))
                    self.events_list.append(event)
                except KeyError:
                    ctx.log.warn("暂无事件!")
                event_list = list(set(self.events_list))

                if not os.path.exists(ST.report_path):
                    os.mkdir(ST.report_path)
                    ctx.log.info(ST.report_path + ' 新建成功！')

                file = open('{}/now_event.txt'.format(ST.report_path), 'w')
                for line in event_list:
                    file.write(line + '\n')
                ctx.log.warn("事件名集合====>{}".format(event_list))
                lost_list = list(set(ST.all_events).difference(set(event_list)))
                ctx.log.warn("丢失事件名====>{}".format(lost_list))
                file = open('{}/lost_event.txt'.format(ST.report_path), 'w')
                for line in lost_list:
                    file.write(line + '\n')
