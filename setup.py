#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="garbevents",
    version="1.0.5",
    keywords=["pip", "garbevents", "get_events", "buried points"],
    description="grabbing buried points",
    long_description="A method of grabbing buried points, improve the mitmproxy."
                     "This is a python toolkit for real-time capture,analysis, "
                     "cleaning and report generation of embedded points based on the development of mitmproxy.",
    license="MIT Licence",

    url="https://github.com/Pactortester/garb-events",
    author="lijiawei",
    author_email="1456470136@qq.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Software Development :: Testing",
        "Typing :: Typed",
    ],

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["mitmproxy"]
)
