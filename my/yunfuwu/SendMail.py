
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import time
import smtplib
import sys
sys.path.append(r"D:\pyproject")
import constant
class SendMail:
    def format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    # 海外在
    def accesssendmail(self,content):
        # self.inland_esend_mail("title",content)
        self.googlesend_mail("title",content)
    def googlesend_mail(self,title,content):
        user_mail = constant.user_mail1
        password = constant.password1
        # 我的重用简单密码
        send_mail = constant.send_mail
        # send_mail = '864932125@qq.com'
        # smtp_server = 'smtp.163.com'

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.format_addr('发件人 <%s>' % user_mail)
        msg['To'] = self.format_addr('收件人了 <%s>' % send_mail)
        msg['Subject'] = Header(title, 'utf-8').encode()

        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
        server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        server.starttls()
        server.set_debuglevel(1)
        server.login(user_mail, password)
        server.sendmail(user_mail, [send_mail], msg.as_string())
        server.quit()


    def inland_esend_mail(self,title,content):
        user_mail = constant.user_mail
        password = constant.password
        # 我的重用简单密码
        send_mail = constant.send_mail
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.format_addr('发件人 <%s>' % user_mail)
        msg['To'] = self.format_addr('收件人了 <%s>' % send_mail)
        msg['Subject'] = Header(title, 'utf-8').encode()
        server = smtplib.SMTP("smtp.163.com", 25, timeout=120)
        server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        server.starttls()
        server.set_debuglevel(1)
        server.login(user_mail, password)
        server.sendmail(user_mail, [send_mail], msg.as_string())
        server.quit()


