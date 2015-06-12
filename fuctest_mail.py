__author__ = 'LP'
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'lvwebmail@126.com'
receiver = '21639736@qq.com'
subject = 'python email test'
smtpserver = 'smtp.126.com'
username = 'lvwebmail@126.com'
password = 'bdvksgjgfhnitemz'

msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()