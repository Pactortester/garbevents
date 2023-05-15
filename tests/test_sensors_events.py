from garbevents.sensors_events import GetData
from garbevents.settings import Settings as ST

"gb -p 8889 -s test_sensors_events.py"
ST.url = "https://sensors.wenwo.com"
ST.report_path = "report"
ST.all_events = [
    "LX_CONVERSATION_MSG_ITEM_FORWAR_CLICK",
    "LX_CONVERSATION_SETTING_TOPS_CLICK",
]

addons = [GetData()]
