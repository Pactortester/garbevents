# -*- coding: utf-8 -*-

"""
Parameter initialization is a global variable by default. When calling the relevant API,
you need to inherit the setting class and set the corresponding parameters.

"""


class Settings(object):
    """
    # 埋点上传url
    ST.url = 'https://www.baidu.com/'
    # 报告生成路径
    ST.report_path = 'report'
    # 所有事件名称
    ST.all_events = ['event_name_1', 'event_name_2']
    # 接口地址
    ST.interface_url = ['apipool', 'APIPOOL']
    """
    report_path = 'report'  # 默认在当前路径生成report文件夹
    url = None
    all_events = []
    interface_url = []
