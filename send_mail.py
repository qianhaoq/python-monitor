#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
# 提供邮件报警功能
# based on Python 2.7
# useage: python compare_commclk_queue.python
"""
import os
import sys
import smtplib
import urllib
import json
import time
import logging
from email.mime.text import MIMEText
from email.header import Header

def senderMail():
    """
    # 邮件发送模块
    # 输入: 错误queue信息,当前时间
    """
    sender = 'qh@qianhao.com'
    receivers = ['qianhaoq@126.com']
    message = MIMEText('http://www.yamibuy.com/cn/goods.php?id=166453', 'plain', 'utf-8')
    #receivers = ['qianhao@baidu.com','zhengxiying@baidu.com']
    # queue_msg = error_time
    # his_list = result_list
    # message = MIMEText('巡查时间:' + str(curt_time)  +
    #         ' \n 请注意,诚信小表拉取数据失败，产出/app/ecom/aries/sf_public/salerules/input/pv_'  \
    #         + queue_msg + ' 的数据失败\n'\
    #         + '重启脚本位于cp01-guarantee-offline.epc.baidu.com机器，重启操作为 cd /home/work/chengxin/industry/tools/salerules/hql/\
    #         && sh getPvDataByHql.sh '+ queue_msg + '\n 历史抓取数据如下:\n' + his_list, 'plain', 'utf-8')
    message['Subject'] = 'this is a test email'
    message['From'] = sender
    #receiver_list = ';'.join(receivers)
    message['To'] =  receivers[0]

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")


def main():
    """
    main function
    """
    # 获取当前时间
    #
    # error_time = sys.argv[1]
    # curt_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # file = open("result_list.txt")
    # result_list = file.read()
    senderMail()

if __name__ == "__main__":
    main()
