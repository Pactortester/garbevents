# -*- coding: utf-8 -*-

import urllib
import zlib
import urllib.parse
import urllib.error
import mitmproxy
from mitmproxy import http
import base64
import json
from garbevents.settings import Settings as ST


class GetData:
    """
    A mitmproxy HTTP request class.
    """
    events_list = []

    @staticmethod
    def chunks(arr, n):
        return [arr[i:i + n] for i in range(0, len(arr), n)]

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """

        :param flow:
        :return:
        """

        request_data = flow.request
        self.request_url = request_data.url
        if ST.url in self.request_url:
            print("url:-------->", self.request_url)
            api = self.request_url.split('/')[3].replace("'", '')
            print("拆分后获取API地址====>", api)
            if api in ST.interface_url:
                request_content = str(flow.request.content).split("event=")[1].replace("'", '').replace(' ', '+')
                print("拆分后获取加密数据====>", request_content)
            else:
                request_content = str(flow.request.url).split('&')[1].split('event=')[1]
                print("拆分后获取加密数据====>", request_content)
            if request_content.find('%') == 0:
                result = urllib.parse.unquote(request_content)
            else:
                url_content = urllib.parse.unquote(request_content)
                a = base64.b64decode(url_content)
                result = zlib.decompress(a).decode('utf-8')
            result_list = json.loads(result)
            try:
                event = result_list["data"][0]["pr"]["$eid"]
                print("解密数据后获取事件名====>", event)
                self.events_list.append(event)
            except KeyError:
                print("暂无事件!")
            event_list = list(set(self.events_list))

            file = open('{}/now_event.txt'.format(ST.report_path), 'w')
            for line in event_list:
                file.write(line + '\n')
            print("事件名集合====>", event_list)
            lost_list = list(set(ST.all_events).difference(set(event_list)))
            print("丢失事件名====>", lost_list)
            file = open('{}/lost_event.txt'.format(ST.report_path), 'w')
            for line in lost_list:
                file.write(line + '\n')
