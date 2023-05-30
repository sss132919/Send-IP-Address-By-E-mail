import socket
import json
import os
import smtplib
import requests
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import asctime

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

def send_an_email(email_content): # email_content是一个字符串
    mail_host = "smtp.163.com" # 这个去邮箱找
    mail_user = "xxxx@163.com" # 邮箱名
    mail_auth_code = "xxxxxxxxxxxxxxx" # 授权码
    mail_sender = mail_user # 用mail_user 作为发送人
    mail_receivers = ["xxxxxxxx@163.com"]
    message = MIMEMultipart()
    message['From'] = Header(mail_sender)  # 寄件人
    message['Subject'] = Header("当前ip地址")
    message.attach(MIMEText(asctime(), 'plain', 'utf-8'))
    message.attach(MIMEText(email_content, 'plain', 'utf-8'))
    print("message is {}".format(message.as_string())) # debug用
    smtpObj = smtplib.SMTP(mail_host)
    # smtpObj.set_debuglevel(1) # 同样是debug用的
    smtpObj.login(mail_user, mail_auth_code) # 登陆
    smtpObj.sendmail(mail_sender, mail_receivers, message.as_string()) # 真正发送邮件就是这里

def getIPv4addr():
    url='http://4.ipw.cn'
    response = requests.get(url,headers = headers)
    print(response.text)
    return response.text

def getIPv6addr():
    url='https://6.ipw.cn'
    response = requests.get(url,headers = headers)
    print(response.text)
    return response.text

if __name__ == "__main__":
    getIPv4addr()
    getIPv6addr()
    send_an_email("\nipv4 address:"+getIPv4addr()+"\nipv6 address:"+getIPv6addr())
    
