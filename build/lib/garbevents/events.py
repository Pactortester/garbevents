# -*- coding: utf-8 -*-
import os
import urllib
import zlib
import urllib.parse
import urllib.error
from pprint import pprint

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
        return [arr[i:i + n] for i in range(0, len(arr), n)]

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """

        :param flow:
        :return:
        """

        request_data = flow.request
        self.request_url = request_data.url
        if ST.url in self.request_url:

            api = self.request_url.split('/')[3].replace("'", '')
            if api in ST.interface_url:
                request_content = str(flow.request.content).split("event=")[1].replace("'", '').replace(' ', '+')
            else:
                request_content = str(flow.request.url).split('&')[1].split('event=')[1]
            if request_content.find('%') == 0:
                result = urllib.parse.unquote(request_content)
            else:
                url_content = urllib.parse.unquote(request_content)
                ace = base64.b64decode(url_content)
                result = zlib.decompress(ace).decode('utf-8')
            result_list = json.loads(result)
            pprint(result_list)
            try:
                event = result_list["data"][0]["pr"]["$eid"]
                ctx.log.error("Get the event name after decrypting the data ====>{}".format(event))
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
