#!/usr/local/bin/python3
# MUA -> MTA ->···-> MTA -> MDA
# MUA和MTA使用的协议, 以及MTA到另一个MTA 都是 SMTP：Simple Mail Transfer Protocol
# MUA和MDA使用的协议有两种:
# POP：Post Office Protocol，目前版本是3，俗称POP3;
# IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件，比如从收件箱移到垃圾箱，等等

import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send(m_target = '996519916@qq.com', m_content = 'send by python', m_title = 'error message'):
    from_address = '940778304@qq.com'
    from_pass = 'bdrtrnotoxodbfej'
    smtp_server = 'smtp.qq.com'
    _target = m_target
    _content = m_content
    _title = m_title

    content = MIMEText(_content, 'plain', 'utf-8')
    content['From'] = from_address
    content['To'] = _target
    content['Subject'] = Header(_title, 'utf-8')


    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(from_address, from_pass)
    server.sendmail(from_address, _target, content.as_string())
    server.quit()
