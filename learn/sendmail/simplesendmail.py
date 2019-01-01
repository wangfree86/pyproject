# -*- coding:UTF-8 -*-
'''
这是一个完整的例子，从163邮箱发送到qq邮箱，注意点密码是邮箱的授权码，自己在网易邮箱设置的
发送邮件至对应的邮箱

'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

# if __name__ == '__main__':
#     send_mail("hahhhh")

import time


class Semd(object):
    def format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_mail(self,content):
        print('000000')  # 输出i
        user_mail = 'wangfree86@gmail.com'
        password = 'xx'
        # 我的重用简单密码
        send_mail = '15038378662@139.com'
        smtp_server = 'smtp.163.com'

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.format_addr('发件人 <%s>' % user_mail)
        msg['To'] = self.format_addr('收件人了 <%s>' % send_mail)
        msg['Subject'] = Header('标题', 'utf-8').encode()
        print('111111111111')  # 输出i
        server = smtplib.SMTP(smtp_server, 25)
        print('22222222')  # 输出i
        server.set_debuglevel(1)
        server.login(user_mail, password)
        print('44444')  # 输出i
        server.sendmail(user_mail, [send_mail], msg.as_string())
        server.quit()


if __name__ == "__main__":
    dl = Semd()
    print('开始执行程序')  # 输出i
    # str='发送数据了：'+'--------'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # dl.send_mail(str)

    i = 1
    while i <= 3:
        print('第'+str(i)+'次发送准备中')  # 输出i
        nstr='第'+str(i)+'次发送:'+'--------'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        dl.send_mail(nstr)
        print(nstr)  # 输出i
        i += 1
        time.sleep(6)  # 休眠 秒

