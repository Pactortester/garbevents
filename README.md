# garbevents


[![Build Status](https://travis-ci.com/Pactortester/garbevents.svg?branch=master)](https://travis-ci.com/Pactortester/garbevents) ![PyPI](https://img.shields.io/pypi/v/garbevents) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/garbevents) ![GitHub top language](https://img.shields.io/github/languages/top/Pactortester/garbevents) ![PyPI - Downloads](https://img.shields.io/pypi/dm/garbevents) ![GitHub stars](https://img.shields.io/github/stars/Pactortester/garbevents?style=social) ![https://blog.csdn.net/flower_drop](https://img.shields.io/badge/csdn-%40flower__drop-orange)


## Logo


![logo](https://github.com/Pactortester/garbevents/blob/master/images/garbevents.png)


## 安装


pip install garbevents


##  仓库地址：


- github：https://github.com/Pactortester/garbevents.git
- pypi：https://pypi.org/project/garbevents/#history


## 社区地址


- testerhome：https://testerhome.com/opensource_projects/garbevents


## 适用场景


1. 使用 诸葛IO 作为埋点收集工具的 。
2. 需要回归验证大批量埋点是否丢失的。
3. 使用本工具 自动抓取解析埋点信息数据校验埋点是否 丢失。


## 功能


1. 自动解析 移动端\桌面端\h5页面 触发的埋点信息，解密后生成[now_data.txt]
2. 去重后和已知埋点信息diff,保存文件[lost_data.txt]


## 使用


- 启动服务
```shell
mitmdump -p 8889
```

- 连接代理

- 下载证书
```shell
mitm.it
```


## 命令


```shell
mitmdump -p 8889 -s <you_test_script.py>
```


## Demo


```python
from garbevents.events import GetData
from garbevents.settings import Settings as ST

# 埋点上传url 
ST.url = 'https://datain.zhuge.com'
# 报告生成路径 
ST.report_path = 'report'
# 所有事件名称 
ST.all_events = ['event_name_1', 'event_name_2']
# 接口地址
ST.interface_url = ['apipool', 'APIPOOL']

addons = [
    GetData()
]
```
## 

以上便是 garbevents 的基本用法介绍。

如果您有发现错误，或者您对 garbevents 有任何建议，欢迎到 [garbevents Issues](https://github.com/Pactortester/garbevents/issues) 发表，非常感谢您的支持。您的反馈和建议非常宝贵，希望您的参与能帮助 garbevents 做得更好。
