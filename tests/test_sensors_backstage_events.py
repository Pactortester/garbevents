# -*- coding: utf-8 -*-

from garbevents.sensors_backstage_event import GetData

from garbevents.settings import Settings as ST

'gb -p 8889 -s test_sensors_backstage_events.py'

ST.url = '/data/logs/sensors/wenwo-cloud-core-domain-doctor-service/'
ST.report_path = 'report'
ST.all_events = ['$WebClick', '$pageview']
ST.events_properties = {
    'graphic_switch': ['status_update', 'doc_set_num', 'doc_set_price', 'doc_set_sever_time']
}
GetData.backstage('server_ip', 'server_name', 'server_password')

addons = [
    GetData()
]
