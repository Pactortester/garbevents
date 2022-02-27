# garbevents

本项目由 [JetBranins](https://www.jetbrains.com/?from=garbevents) 赞助相关开发工具  
<a href="https://www.jetbrains.com/?from=garbevents"><img src="https://files.mdnice.com/user/17535/b66e2763-ae98-4d2d-b239-4ab35c0a878c.svg" width = "150" height = "150" div align=center /></a>

##  

[![Build Status](https://travis-ci.com/Pactortester/garbevents.svg?branch=master)](https://travis-ci.com/Pactortester/garbevents) ![PyPI](https://img.shields.io/pypi/v/garbevents) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/garbevents) ![GitHub top language](https://img.shields.io/github/languages/top/Pactortester/garbevents) [![Downloads](https://static.pepy.tech/personalized-badge/garbevents?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads/total)](https://pepy.tech/project/garbevents) ![GitHub stars](https://img.shields.io/github/stars/Pactortester/garbevents?style=social) ![https://blog.csdn.net/flower_drop](https://img.shields.io/badge/csdn-%40flower__drop-orange)


## 埋点适配计划

- [x] 诸葛 IO
- [x] 神策数据
- [x] GrowingIO 埋点数据
- [x] Argo 易观方舟
- [ ] 友盟
- [ ] C4J
- [ ] Mixpanel 
- [ ] GA 
- [ ] Ptmind Ptengine
- [ ] 国双 WebDissector
- [ ] 谷歌分析 Google Analytics
## Logo

![](https://files.mdnice.com/user/17535/ed606252-d4db-42b0-9081-a81c438d1eab.png)

## 安装

pip install garbevents

## 仓库地址：

- github：https://github.com/Pactortester/garbevents.git
- pypi：https://pypi.org/project/garbevents/#history

## 社区地址

- testerhome：https://testerhome.com/opensource_projects/garbevents

## 适用场景

1. 使用 以上厂商 作为埋点收集工具的 。
2. 需要回归验证大批量埋点是否丢失的。
3. 使用本工具 自动抓取解析埋点信息数据校验埋点是否 丢失。

## 功能

1. 自动解析 移动端\桌面端\h5页面 触发的埋点信息，解密后生成 [now_data.txt]()
2. 去重后和已知埋点信息diff,保存文件 [lost_data.txt]()

## 使用

- 启动服务

1. 在cmd启动代理服务

```shell
gb -p 8889 -s test_script.py

                     __                         __      
   ____ _____ ______/ /_  ___ _   _____  ____  / /______
  / __ `/ __ `/ ___/ __ \/ _ \ | / / _ \/ __ \/ __/ ___/
 / /_/ / /_/ / /  / /_/ /  __/ |/ /  __/ / / / /_(__  ) 
 \__, /\__,_/_/  /_.___/\___/|___/\___/_/ /_/\__/____/  v2.0.5
/____/ 

Proxy server listening at http://*:8889

```

- 连接代理

1. cmd中运行ipconfig 找到自己的ip地址
2. 手机wifi高级选项，代理选择手动，添加代理服务器

```shell
ip:你的电脑ip, 端口:8889
```

- 下载证书

1. 在手机浏览器中打开网址 [mitm.it]()
2. 选择对应的证书下载安装

```shell
mitm.it
```

- 开始使用

1. 此时便可以在手机端操作触发埋点，控制台实时打印当前触发的埋点
2. 如果想查看丢失的埋点需要先在 ST.all_events 全局变量中传入全部埋点信息
3. 例如：ST.all_events = ['event_name_1', 'event_name_2']

## 命令

```shell
# 只打印所需日志
gb -p 8889 -q -s test_script.py
```

## 诸葛IO Demo

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

## 神策数据 Demo 1

```python
from garbevents.sensors_events import GetData
from garbevents.settings import Settings as ST

# 埋点上传url 
ST.url = 'http://sensor.wodidashi.com'
# 报告生成路径 
ST.report_path = 'report'
# 所有事件名称 
ST.all_events = ['event_name_1', 'event_name_2']

addons = [
    GetData()
]
```
## 神策数据 Demo 2

```python
from garbevents.custom_sensors_events import GetData
from garbevents.settings import Settings as ST

# 埋点上传url 
ST.url = 'http://sensor.wodidashi.com'
# 报告生成路径 
ST.report_path = 'report'
# 所有事件名称 
ST.all_events = ['event_name_1', 'event_name_2']

addons = [
    GetData()
]
```

## GrowingIO Demo

```python
from garbevents.growingio_events import GetData
from garbevents.settings import Settings as ST

# 埋点上传url 
ST.url = 'https://wxapi.growingio.com'
# 报告生成路径 
ST.report_path = 'report'
# 所有事件名称 
ST.all_events = ['event_name_1', 'event_name_2']
addons = [
    GetData()
]

```

## Argo 易观方舟 Demo

```python
from garbevents.argo_events import GetData
from garbevents.settings import Settings as ST

# 埋点上传url 
ST.url = 'https://uat.analysys.cn:4089/'
# 报告生成路径 
ST.report_path = 'report'
# 所有事件名称 
ST.all_events = ['event_name_1', 'event_name_2']
addons = [
    GetData()
]

```

## 运行截图

![](https://files.mdnice.com/user/17535/c730acf2-ec15-4924-9cf5-b0b77c092211.png)


## 用法拓展

1. 结合UI自动化，嵌入到你的平台或者框架中，运行自动化脚本的同时，也测试了埋点。
2. 部署到公司服务器，给测试部门的同学用，助人为乐！！！

##  

以上便是 garbevents 的基本用法介绍。

如果您有发现错误，或者您对 garbevents 有任何建议，欢迎到 [garbevents Issues](https://github.com/Pactortester/garbevents/issues)
发表，非常感谢您的支持。您的反馈和建议非常宝贵，希望您的参与能帮助 garbevents 做得更好。
