#!/usr/bin/python3
import os
import urllib.request
import gzip
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 伪装User-Agent
header = {}
header['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"

# 设定监控的url
url1 = "http://www.yamibuy.com/cn/goods.php?id=166453"
id1 = 166453

url2 = "http://www.yamibuy.com/cn/goods.php?id=164114"
id2 = 164114

item_list = {}
item_list[id1] = url1
item_list[id2] = url2

info_list = {}
info_list[id1] = "好欢螺 螺蛳粉 400g 到货啦！ "
info_list[id2] = "好欢螺 螺蛳粉 300g 到货啦！ "

# 获取当前目录
path = os.getcwd()
# 设定锁目录
filename = path + '//' + 'lock.txt'

def senderMail(idx):
    """
    # 邮件发送模块
    """
    sender = 'qh@qianhao.com'
    receivers = ['qianhaoq@126.com']
    message = MIMEText(info_list[idx] + "\n购买地址为: " + item_list[idx], 'plain', 'utf-8')

    message['Subject'] = '好欢螺到货通知！'
    message['From'] = sender
    #receiver_list = ';'.join(receivers)
    message['To'] =  receivers[0]

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

def listen_url(url, idx):
    print(url,idx)
    req = urllib.request.Request(url, headers = header)
    response = urllib.request.urlopen(req)
    data = response.read()
    try:
        html = gzip.decompress(data).decode("utf-8")
    except:
        html = data.decode("utf-8")
    if html.find('已售完') < 0:
        f = open(filename, 'w')
        f.close()
        senderMail(idx)



if os.path.exists(filename):
    exit()
listen_url(url1, id1)
listen_url(url2, id2)
# print(listen_url(url2))
