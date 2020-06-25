# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 19:39
# @Author  : 李佳玮
# @Email   : lijiawei@symbio.com
# @File    : test_events.py
# @Software: PyCharm

from garbevents.events import GetData

from garbevents.settings import Settings as ST


'mitmdump -p 8889 -s test_events.py'


ST.url = 'https://www.baidu.com/'
ST.report_path = 'report'
ST.all_events = ['LX_CONVERSATION_MSG_ITEM_FORWAR_CLICK', 'LX_CONVERSATION_SETTING_TOPS_CLICK']
ST.interface_url = ['apipool', 'APIPOOL']

addons = [
    GetData()
]
