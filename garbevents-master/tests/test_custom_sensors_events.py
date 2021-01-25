# -*- coding: utf-8 -*-

from garbevents.custom_sensors_events import GetData


from garbevents.settings import Settings as ST

'mitmdump -p 8889 -q -s test_custom_sensors_events.py'

# https://sensors.wenwo.com 爱问医生
ST.url = 'https://sensors.wenwo.com'
ST.report_path = 'report'
ST.all_events = ['$WebClick', '$pageview']
ST.events_properties = {
    '$WebClick': ['app_name', 'is_login','part_name','platform_type','referrer_path'],
    '$pageview':[ 'app_name','is_login','part_name','platform_type','referrer_path']
}

addons = [
    GetData()
]
