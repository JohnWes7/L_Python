# POP3/SMTP password kqnxgxrcdibrfjaj kqnx gxrc dibr fjaj

from email.mime import text
import os
from config import config
from email import header
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_simple():
    # 登录邮箱
    smtp_obj = smtplib.SMTP('smtp.qq.com')
    smtp_obj.login('1246215651@qq.com', 'kqnxgxrcdibrfjaj')

    # 编写内容
    # 字符串内容
    msg = '测试字符串内容'

    # html内容
    file = open(config.absolute_data_PATH+'/msg.html', 'r', encoding='utf-8')
    msg = file.read()

    # email = MIMEText(msg, 'plain', 'utf-8')
    email = MIMEText(msg, 'html', 'utf-8')

    email['Subject'] = Header('测试python邮件', 'utf-8')
    email['From'] = Header('Johnwest', 'utf-8')

    # 发送
    smtp_obj.sendmail('1246215651@qq.com',
                      ['mrlyjcqc@163.com'], email.as_bytes())
    print("send successful")
    smtp_obj.quit()


def MIMEMultipart_email():
    # 邮件
    # 主题文字
    html = open(config.absolute_data_PATH+'/msg.html',
                'r', encoding='utf-8').read()
    textApart = MIMEText(html, 'html', 'utf-8')
    # 附件图片
    imageApart = MIMEImage(
        open(config.absolute_data_PATH+'/test_image.jpg', 'rb').read(), 'jpg')
    imageApart.add_header('content-disposition',
                          'attachment', filename='test_jpg.jpg')

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(imageApart)

    m['Subject'] = Header('测试附件', 'utf-8')

    # 发送
    print('开始发送')
    smtp = smtplib.SMTP('smtp.qq.com')
    smtp.login('1246215651@qq.com', 'kqnxgxrcdibrfjaj')
    smtp.sendmail('1246215651@qq.com',
                  ['mrlyjcqc@163.com'], m.as_bytes())
    print("send successfil")
    smtp.quit()
    # try:

    # except:
    #     print('发送失败')


if __name__ == "__main__":
    # send_simple()
    MIMEMultipart_email()
