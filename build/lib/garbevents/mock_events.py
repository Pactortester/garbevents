# -*- coding: utf-8 -*-
from pprint import pprint
from mitmproxy import ctx
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

    def response(self, flow):
        """
        mock修改响应接口
        :param flow:
        :return:
        """
        if flow.request.url.startswith(ST.url):
            response = json.loads(flow.response.get_text())
            pprint(response)
            ctx.log.warn('-------------------------Dividing line---------------------------')
            res = flow.response.set_text(json.dumps(ST.mock_json))
            pprint(res)
            ctx.log.warn('modify success')

