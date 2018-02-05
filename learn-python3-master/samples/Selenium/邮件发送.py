#!/usr/bin/env python3
# -*- coding: utf-8 -*
import smtplib
#邮件文件类型
from  email.mime.text import MIMEText
from  email.header import Header
from  email.mime.application import MIMEApplication
from  email.mime.multipart import  MIMEMultipart

#设置qq邮箱服务器地址和端口号
smtp_qq_server = 'smtp.qq.com'
qq_sort = "465"

from_email = "1925023449@qq.com"
#服务器授码
mail_pass = "gmyuchkzxdibfddb"
to_mail = "1925023449@qq.com" #"1925023449@qq.com,1@qq.com"
msg = MIMEMultipart()#发送的文件类型
msg["From"]=from_email
msg["To"]=to_mail
#邮件标题 ,中文需要转码
msg["Subject"]=Header('自动化测试报告，请查收','utf-8').encode()
#邮件正式的内容
textPart = MIMEText(u"自动化测试")
msg.attach(textPart)
#附件内容-以图片为例,我自己的邮箱发给自己

"""
#xlsx类型附件
XlsxPart = MIMEApplication(open(r'E:\test.xlsx','rb').read())
XlsxPart.add_header('Content-Disposition', 'attachment', filename="test.xlsx")
msg.attach(XlsxPart)

#jpg类型附件
PicturePart = MIMEApplication(open(r'E:\test.jpg','rb').read())
PicturePart.add_header('Content-Disposition', 'attachment', filename="test.jpg")
msg.attach(PicturePart)

#pdf类型附件
PdfPart = MIMEApplication(open(r'E:\test.pdf','rb').read())
PdfPart.add_header('Content-Disposition', 'attachment', filename="test.pdf")
msg.attach(PdfPart)

#mp3类型附件
MP3Part = MIMEApplication(open(r'E:\test.mp3','rb').read())
MP3Part.add_header('Content-Disposition', 'attachment', filename="test.mp3")
msg.attach(MP3Part)
"""

picture = MIMEApplication(open(r"C:\Users\dujuan\Desktop\images\images.png",'rb').read())
picture.add_header('Content-Disposition','attachment',filename = 'images.png')
msg.attach(picture)

try:
    s = smtplib.SMTP_SSL(smtp_qq_server,qq_sort)
    s.connect(smtp_qq_server)
    s.login(from_email,mail_pass)
    #  # as_string()把MIMEText对象变成str
    s.sendmail(from_email,to_mail,msg.as_string())
    s.quit()
except smtplib.SMTPException as  e:
    print(e)
