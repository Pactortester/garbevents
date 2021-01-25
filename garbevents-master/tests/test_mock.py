# -*- coding: utf-8 -*-

from garbevents.events import GetData

from garbevents.settings import Settings as ST

'mitmdump -p 8889 -s test_events.py'
ST.url = 'https://www.company.com'

ST.mock_json = {"code": "0", "msg": "success", "data": {"demo"}}

addons = [
    GetData()
]
