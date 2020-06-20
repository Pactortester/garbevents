# garb-events

## 依赖环境

pip install -r requirements.txt

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
mitmdump -p 8889 -s op.py
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

addons = [
    GetData()
]
```


