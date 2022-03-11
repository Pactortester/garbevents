# -*- coding: utf-8 -*-

from garbevents.mock_events import GetData

from garbevents.settings import Settings as ST

'gb -p 8889 -s test_events.py'
ST.url = 'https://www.company.com'

ST.mock_json = {"code": "0", "msg": "success", "data": {"demo"}}

addons = [
    GetData()
]
