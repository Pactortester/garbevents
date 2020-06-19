# -*- coding: utf-8 -*-
# @Time    : 2019/11/4 8:49
# @Author  : 李佳玮
# @Email   : 1456470136@qq.com
# @File    : events.py
# @Software: PyCharm


import urllib
import zlib
import urllib.parse
import urllib.error
import mitmproxy
from mitmproxy import http
import base64
import json

'''
启动命令 

mitmdump -p 8889
下载证书
mitm.it

连接代理

运行命令
mitmdump -p 8889 -s mobile_op.py
mitmweb -p 8889 -s mobile_op.py

addons = [
    get_events()
]


'''

# 生成一个埋点列表
events_list = []


# 拿到请求数据
def get_events(url, all_events, report_path):
    """

    :param url: 埋点地址
    :param all_events: 事件list
    :param report_path: 生成报告路径
    :return:
    """
    flow = mitmproxy.http.HTTPFlow
    request_data = flow.request

    # print(request_data)
    # 请求地址
    request_url = request_data.url

    # 通过网址过滤 只打印预期网址的返回
    if url in request_url:
        print("url:-------->", request_url)
        api = request_url.split('/')[3].replace("'", '')
        print("拆分后获取API地址====>", api)
        if api == "APIPOOL":
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
            events_list.append(event)
        except KeyError:
            print("暂无事件!")
        # 去重
        event_list = list(set(events_list))

        file = open('{}/now_event.txt'.format(report_path), 'w')
        for line in event_list:
            file.write(line + '\n')

        print("事件名集合====>", event_list)
        # 所有的埋点事件

        lost_list = list(set(all_events).difference(set(event_list)))
        print("丢失事件名====>", lost_list)

        file = open('{}/lost_event.txt'.format(report_path), 'w')
        for line in lost_list:
            file.write(line + '\n')
            # file.close()
