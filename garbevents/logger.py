# -*-coding:utf8-*-
"""
============================
# -*- coding: utf-8 -*-
# @Author  : 晴天
============================
"""
import logging
# 读取配置文件中相关数据
import os


# from medical_care_assets.common.constant import LOG_DIR
#
# from medical_care_assets.common.config import conf


# 第二种封装方式
class MyLogging:

    def my_log(self, level, msg):

        # 写一个属于自己的日志系统
        # 收集器--创建一个日志收集器getLogger函数
        my_logger = logging.getLogger('Aiwen_Doctor')  # 创建一个日志收集器
        my_logger.setLevel('DEBUG')  # 给这个日志收集器设置一个等级

        # 格式：规定日志输出的格式
        formatter = logging.Formatter('%(asctime)s-'
                                      '[ %(levelname)s]-'
                                      '[日志信息]:%(message)s')

        # 输出渠道--指定输出渠道
        ch = logging.StreamHandler()  # 创建一个输出到控制台的渠道
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)

        # 输出到之指定的文件  文件路径  绝对路径  相对路径  都可以用
        # 备注需要写自己当前文件的路径
        fh = logging.FileHandler(r'C:\Users\DOCTOR\PycharmProjects\garbevents-master\logs\Event.log', encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 对接日志收集器与输出渠道 进行拼接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        # 去掉日志的重复，每次收集完毕之后，记得移除日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):  # 输出一条debug级别的信息
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)


if __name__ == '__main__':
    AAA = MyLogging()
    AAA.info("晴天")
