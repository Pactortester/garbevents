# -*- coding: utf-8 -*-

from garbevents.custom_sensors_events import GetData


from garbevents.settings import Settings as ST

'mitmdump -p 8889 -s test_custom_sensors_events.py'

# https://sensors.wenwo.com 爱问医生
# http://sensorsdata-2.talbrain.com:8106 学而思网校
ST.url = 'https://sensors.wenwo.com'
ST.report_path = 'report'
ST.all_events = ['LX_CONVERSATION_MSG_ITEM_FORWAR_CLICK', 'LX_CONVERSATION_SETTING_TOPS_CLICK']

addons = [
    GetData()
]
