# garbevents

## 安装

pip install garbevents

## 适用场景

1. 诸葛io是数据智能收集，其核心在于对用户行为的深入分析与洞察，支持前端代码埋点、全埋点、可视化圈选埋点及服务端采集等多种技术方案，利用实时数据进行高效自动化运营。
2. 自动抓取解析埋点信息数据校验埋点是否丢失。

## 功能

1. 自动解析移动端触发的埋点信息，解密后生成[now_data.txt]
2. 去重后和已知埋点信息diff,保存文件[data.txt]


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
ST.url = 'https://www.baidu.com/'
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


