# coding=utf-8
from bs4 import BeautifulSoup
from SendMail import *
import requests
import time
class getJianshu:
    def __init__(self):
        self.ttime = 0
        # 简书是否日更
        self.janshucom = False
        self.server = 'https://www.jianshu.com/u/5b4978fe1f2a'

        # 还原初始化之，每天零点还原一次
    def restoretime(self):
        ntime = time.strftime("%H", time.localtime())
        if '00' == ntime:
            self.ttime = 0
            self.janshucom = False



        # 重点监控简书是否日更了，20点后每10分钟监听一次，知道完成在停止
    def jianshu(self):
        ntime = time.strftime("%H", time.localtime())
        htime = int(ntime)
        if htime >= 21 and False == self.janshucom:
            self.ttime = self.ttime + 1
            print('查询简书了' + str(self.ttime))
            self.queryjianshu(self.ttime)

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
            SendMail().accesssendmail(s)
        else:
            s = '无日更！！！！第' + str(num) + '次提醒'
            print(s)
            SendMail().accesssendmail(s)