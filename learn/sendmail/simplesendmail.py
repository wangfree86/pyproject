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


class downloader(object):
    def format_addr(self,s):
            name, addr = parseaddr(s)
            return formataddr((Header(name, 'utf-8').encode(), addr))
    def send_mail(self):
            user_mail = '18612079017@163.com'
            password = 'xxx'
            # 我的重用简单密码
            send_mail = '864932125@qq.com'
            smtp_server ='smtp.163.com'

            msg = MIMEText('正文内容不错', 'plain', 'utf-8')
            msg['From'] =self.format_addr('发件人 <%s>' % user_mail)
            msg['To'] = self.format_addr('收件人了 <%s>' % send_mail)
            msg['Subject'] = Header('标题', 'utf-8').encode()

            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(user_mail, password)
            server.sendmail(user_mail, [send_mail], msg.as_string())
            server.quit()
if __name__ == "__main__":
    dl = downloader()
    dl.send_mail()