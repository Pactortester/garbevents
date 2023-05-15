from garbevents.events import GetData
from garbevents.settings import Settings as ST

"gb -p 8889 -s test_events.py"
ST.url = "https://datain.zhuge.com"
ST.report_path = "report"
ST.all_events = [
    "LX_CONVERSATION_MSG_ITEM_FORWAR_CLICK",
    "LX_CONVERSATION_SETTING_TOPS_CLICK",
]
ST.interface_url = ["apipool", "APIPOOL"]

addons = [GetData()]
