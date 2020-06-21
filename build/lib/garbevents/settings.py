# -*- coding: utf-8 -*-

"""
Parameter initialization is a global variable by default. When calling the relevant API,
you need to inherit the setting class and set the corresponding parameters.

"""


class Settings(object):
    report_path = None
    url = None
    all_events = []
    interface_url = None
