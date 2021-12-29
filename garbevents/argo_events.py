# -*- coding: utf-8 -*-
import gzip
import os
import urllib
import urllib.parse
import urllib.error
from pprint import pprint

import mitmproxy
from mitmproxy import http
from mitmproxy import ctx
import json
from garbevents.settings import Settings as ST


class GetData:
    """
    Personal customized version of Argo(易观方舟)
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
        代理服务数据分析
        :param flow:
        :return:
        """

        request_data = flow.request
        self.request_url = request_data.url

        if ST.url in self.request_url:

            ctx.log.info("Get the complete URL after splitting ====>{}".format(self.request_url))
            api = self.request_url.split('/')[3].split('?')[0]
            ctx.log.error("Get API address after splitting ====>{}".format(api))

            request_content = flow.request.content.decode('utf8', errors='ignore')
            ctx.log.info("Get encrypted data after splitting ====>{}".format(request_content))

            gzip_data = urllib.parse.unquote(request_content)
            data_list = json.loads(gzip_data)

            for result_list in data_list:
                ctx.log.error("Get JSON string after decrypting data ====>")
                pprint(result_list)

                try:
                    event = result_list["xwhat"]
                    ctx.log.error("Get the event name after decrypting the data ====> {}".format(event))
                    self.events_list.append(event)
                except KeyError:
                    ctx.log.warn("No events！")
                event_list = list(set(self.events_list))

                if not os.path.exists(ST.report_path):
                    os.mkdir(ST.report_path)
                    ctx.log.info(ST.report_path + 'Successfully created！')

                file = open('{}/now_event.txt'.format(ST.report_path), 'w')
                for line in event_list:
                    file.write(line + '\n')
                ctx.log.warn("Current event name collection ====>{}".format(event_list))
                lost_list = list(set(ST.all_events).difference(set(event_list)))
                ctx.log.warn("Missing event name collection ====>{}".format(lost_list))
                file = open('{}/lost_event.txt'.format(ST.report_path), 'w')
                for line in lost_list:
                    file.write(line + '\n')
