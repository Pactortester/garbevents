#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="garbevents",
    version="1.0.2",
    keywords=["pip", "garbevents", "get_events"],
    description="grabbing buried points",
    long_description="A method of grabbing buried points, improve the mitmproxy",
    license="MIT Licence",

    url="https://github.com/Pactortester/garb-events",
    author="lijiawei",
    author_email="1456470136@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["mitmproxy"]
)
