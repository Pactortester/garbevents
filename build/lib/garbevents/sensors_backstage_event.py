# -*- coding: utf-8 -*-
import gzip
import os
from pprint import pprint
from collections import Counter
import json
import jsonpath
from mitmproxy import ctx

from garbevents.settings import Settings as ST
from datetime import datetime
import paramiko
import select


class GetData:
    """
    Capture of buried points in the background.
    A engine HTTP request class.
    """
    events_list = []
    now_time = datetime.now()
    new_time = now_time.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def chunks(arr, n):
        """

        :param arr:
        :param n:
        :return:
        """
        return [arr[i:i + n] for i in range(0, len(arr), n)]

    @staticmethod
    def gzip_decompress(data):
        """
        解密上报数据
        :param data:
        :return:
        """
        try:
            return gzip.decompress(data)
        except AttributeError:
            from io import StringIO

            buf = StringIO()
            buf.write(data)
            fd = gzip.GzipFile(fileobj=buf, mode="r")
            fd.rewind()
            value = fd.read()
            fd.close()
            return value

    @staticmethod
    def backstage(serverip, user, pwd):
        """
        # 备注:图文咨询设置埋点地址
        # ST.url = '/data/logs/sensors/wenwo-cloud-core-domain-doctor-service/'
        # 医生认证审核埋点地址
        # ST.url='/data/logs/sensors/doctor-background/'+log
        # 电话咨询设置埋点地址
        # ST.url='/data/logs/sensors/wenwo-cloud-doctor-telephone-consultation/'+log
        # 订单相关埋点地址
        # ST.url='/data/logs/sensors/wenwo-cloud-doctor-atomic-information/'+log

        ST.all_events = ['graphic_switch', '测试缺失的事件01', '测试缺失的事件02']
        ST.events_properties = {
            'graphic_switch': ['status_update', 'doc_set_num', 'doc_set_price', 'doc_set_sever_time']
        }
        :param serverip:
        :param user:
        :param pwd:
        :return:
        """
        events_list = []
        # 构造当天的日志文件名字，根据不同的埋点名称再做修改
        now_time = datetime.now()
        new_time = now_time.strftime('%Y-%m-%d')
        log = 'sensors.log.' + new_time

        # 进行连接
        ctx.log.info('------------开始连接服务器(%s)-----------' % serverip)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ctx.log.info('------------开始认证......-----------')
        client.connect(serverip, 22, username=user, password=pwd, timeout=4)
        ctx.log.info('------------认证成功!.....-----------')
        # 开启channel 管道
        transport = client.get_transport()
        channel = transport.open_session()
        channel.get_pty()
        # 执行命令nohup.log.2017-12-30
        tail = 'tail -n 0 -f  ' + ST.url + log
        # 将命令传入管道中
        channel.exec_command(tail)
        while True:
            # 用于精确查出什么时间时候没有值
            news_time = now_time.strftime('%Y-%m-%d %H:%M:%S')

            # 判断退出的准备状态
            if channel.exit_status_ready():
                break
            try:
                # 通过socket进行读取日志，linux相当于客户端
                rl, wl, el = select.select([channel], [], [])
                if len(rl) > 0:
                    recv = channel.recv(1024)
                    # 此处将获取的数据解码成utf-8的读取
                    AAA = recv.decode('utf-8', 'ignore')
                    BBB = AAA.split('\n')
                    DDD = BBB[0:2]
                    for CCC in DDD:
                        try:
                            GGG = str(CCC)
                            data = json.loads(GGG)
                            try:
                                event = data["event"]
                                if event in ST.all_events:
                                    ctx.log.info("【后端】获取到的埋点事件名称是 ====>{}".format(event))
                                    events_list.append(event)
                                    count = Counter(events_list)
                                    lost_list = list(set(ST.all_events).difference(set(events_list)))

                                    # 用于遍历对应event事件里面的具体信息
                                    for event_value in ST.events_properties[event]:
                                        # 记录下坑，下面不能直接在里面传event_value不然取不到值
                                        result = jsonpath.jsonpath(data, f"$..{event_value}")
                                        if result is False:
                                            ctx.log.info("【后端】请注意！！！请注意！！！{}事件未获取到{}值".format(event, event_value))
                                            with open('{}/【后端】埋点事件参数没有值的统计.txt'.format(ST.report_path), 'a+',
                                                      encoding='utf-8') as file01:
                                                # 用于记录埋点事件参数没有值的统计.txt
                                                file01.write("【后端】{}请注意！！！请注意！！！{}事件未获取到{}值!!!".format(news_time, event,
                                                                                                       event_value) + '\n')
                                        else:
                                            ctx.log.info(
                                                "【后端】获取到的埋点事件:{}的自定义参数{}的值是{}：".format(event, event_value, result))

                                    # 在已上报的埋点事件统计.txt记录已经获取到的事件
                                    with open('{}/【后端】已上报的埋点事件统计.txt'.format(ST.report_path), 'w',
                                              encoding='utf-8') as file03:
                                        # file03.writelines(events_list)
                                        for line in events_list:
                                            file03.write(line + '\n')

                                    # 在漏上报的埋点事件统计.txt记录已经获取到的事件
                                    with open('{}/【后端】漏上报的埋点事件统计.txt'.format(ST.report_path), 'w',
                                              encoding='utf-8') as file04:
                                        # file04.writelines(lost_list)
                                        for lines in lost_list:
                                            file04.write(lines + '\n')
                                            ctx.log.info('【后端】暂未获取到这些埋点事件，可能存在漏上报事件 ====>{}'.format(lines))

                                    ctx.log.info('【后端】累计的埋点事件统计次数{}'.format(count))
                                    with open('{}/【后端】累计的埋点事件统计次数.txt'.format(ST.report_path), 'w',
                                              encoding='utf-8') as file02:
                                        # 用于记录埋点事件参数没有值的统计.txt
                                        file02.write("【后端】累计统计到的埋点次数{}!!!".format(count) + '\n')

                                    # 不存在对应txt文件时，先创建txt文件
                                    if not os.path.exists(ST.report_path):
                                        os.mkdir(ST.report_path)
                                        ctx.log.info(ST.report_path + 'Successfully created！')
                                else:
                                    ctx.log.info("该事件{}不在你录的事件中".format(event))
                            except Exception:
                                ctx.log.info('json中不存在event字段,请查看上面具体json查询想要的内容字段')
                                pprint('json中不存在event字段{}'.format(data))
                                break
                        except json.decoder.JSONDecodeError as e01:
                            pass
                        except Exception as e02:
                            print(e02)
                            ctx.log.info("读取不到日志文件，还未生成，请先手动触发事件生成日志")

            # 键盘终端异常
            except KeyboardInterrupt:
                print("Caught control-C")
                channel.send("\x03")  # 发送 ctrl+c
                channel.close()
        client.close()
