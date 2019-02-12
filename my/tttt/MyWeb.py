# coding=utf-8
from bs4 import BeautifulSoup

import requests

# 获取我的简书信息判断是否日更了，没有日更就提醒
# 1.需要添加header针对简单的反爬虫
# 2.保存到cvs
# 3.类内部调用的函数默认都会有一个默认self，需要注意
# 4.每次休息0.1秒，9800篇文章，预计1.5分钟+完成，

class getjianshu:
    def __init__(self):
        self.server = 'https://www.jianshu.com/u/5b4978fe1f2a'
        # 简书是否日更
        self.janshucom = False
        self.ttime = 0

    def queryjianshu(self,num):
        url = self.server
        # 添加headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        # 根据条件筛选元素
        divs = soup.find_all('span', class_="time")
        completed = False
        for tex in divs:
            # 寻找写作的时间，如果有今天时间就日更完成，不然提醒
            writertime = tex.get('data-shared-at')[0:10]
            ntime = time.strftime("%Y-%m-%d", time.localtime())
            if writertime == ntime:
                completed = True
        # completed判断是否写作完成了
        if completed:
            self.janshucom = True
            s = '很好完成日更了'
            sendMail().accesssendmail(s)
        else:
            s = '无日更！！！！第' + str(num) + '次提醒'
            print(s)
            sendMail().accesssendmail(s)

    #测试用的只要是指定整点就发送一次邮件
    def testsendmail(self):

        ntime = int(time.strftime("%H", time.localtime()))
        mtime = int(time.strftime("%M", time.localtime()))
        # 3的倍数时间，分钟小于10分钟时候发送一次
        if ntime%3==0 and mtime<10:
            sendMail().accesssendmail('3小时提醒一次'+str(ntime)+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


    # 一直执行的程序


    # 重点监控简书是否日更了，20点后每10分钟监听一次，知道完成在停止
    def jianshu(self):
        ntime = time.strftime("%H", time.localtime())
        htime = int(ntime)
        if htime >= 20 and False == self.janshucom:
            self.ttime=self.ttime+1
            print('查询简书了'+str(self.ttime))
            self.queryjianshu(self.ttime)

    # 还原初始化之，每天零点还原一次
    def restoretime(self):
        ntime = time.strftime("%H", time.localtime())
        if '00' == ntime:
            self.janshucom = False
            self.ttime=0
    def execute1(self):
        # 一直开启的循环10分钟执行一次任务，不停止
        i=0
        while 1 <= 2:
            # 还原初始化之，每天零点还原一次
            nstr=str(i)+'循环执行中:'+'--------'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            i+=1
            print(nstr)  # 输出i
            self.restoretime()
            self.jianshu()
            self.testsendmail()
            #time.sleep(30)  # 休眠 秒
            time.sleep(60*10)  # 休眠 秒




from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import time
import smtplib




class sendMail:
    def format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    # 海外在
    def accesssendmail(self,content):
        # self.inland_esend_mail(content)
        self.googlesend_mail(content)
    def googlesend_mail(self,content):
        user_mail = 'wangfree86@gmail.com'
        password = 'xx'
        # 我的重用简单密码
        send_mail = '15038378662@139.com'
        # send_mail = '864932125@qq.com'
        # smtp_server = 'smtp.163.com'

        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.format_addr('发件人 <%s>' % user_mail)
        msg['To'] = self.format_addr('收件人了 <%s>' % send_mail)
        msg['Subject'] = Header('3h标题success', 'utf-8').encode()

        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
        server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        server.starttls()
        server.set_debuglevel(1)
        server.login(user_mail, password)
        server.sendmail(user_mail, [send_mail], msg.as_string())
        server.quit()


    def inland_esend_mail(self,content):
        user_mail = '18612079017@163.com'
        password = 'xx'
        # 我的重用简单密码
        send_mail = '15038378662@139.com'
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.format_addr('发件人 <%s>' % user_mail)
        msg['To'] = self.format_addr('收件人了 <%s>' % send_mail)
        msg['Subject'] = Header('3h标题success', 'utf-8').encode()
        server = smtplib.SMTP("smtp.163.com", 25, timeout=120)
        server.ehlo()  # 向Gamil发送SMTP 'ehlo' 命令
        server.starttls()
        server.set_debuglevel(1)
        server.login(user_mail, password)
        server.sendmail(user_mail, [send_mail], msg.as_string())
        server.quit()



