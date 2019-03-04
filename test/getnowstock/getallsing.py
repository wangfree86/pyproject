# coding=utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import requests
import time

import re
import requests, json


class downloader(object):
    def __init__(self):
        self.base = 'https://www.joinquant.com/post/11567?f=sharelist&m=list'
        self.cookies = {}  # 初始化cookies字典变量


    def getcookie(self):
        f = open(r'test.txt', 'r')  # 打开所保存的cookies内容文件
        for line in f.read().split(';'):  # 按照字符：进行划分读取
            # 其设置为1就会把字符串拆分成2份
            name, value = line.strip().split('=', 1)
            self.cookies[name] = value  # 为字典cookies添加内容



    def getmp3url(self, str):
        backtestId='backtestId=a8616c452ac69f5469201c53459af766'
        u1="https://www.joinquant.com/algorithm/live/sharePosition?isAjax=1&backtestId="+backtestId+"&date=2019-03-04&isMobile=0&checkValue=right&isForward=1&ajax=1"
        u2="https://www.joinquant.com/algorithm/live/shareTransaction?isAjax=1&backtestId="+backtestId+"&date=2019-03-04&checkValue=right&isMobile=0&isForward=1&ajax=1"
        # 获取网页内容
        res = requests.get(u1, cookies=self.cookies)
        res.encoding='utf-8'
        html=res.text
        soup = BeautifulSoup(html, features='lxml')

        div = soup.find_all('tr')[0].find_all('td')
        print(div[0].text)
        print(div[1].text)
        print(div[2].text)
    import time

    def get2(self, str):
        backtestId='a8616c452ac69f5469201c53459af766'
        backtestId='4e20d850b00d3e44f6cbb13ecffccf1e'
        u1="https://www.joinquant.com/algorithm/live/sharePosition?isAjax=1&backtestId="+backtestId+"&date=2019-03-04&isMobile=0&checkValue=right&isForward=1&ajax=1"
        u2="https://www.joinquant.com/algorithm/live/shareTransaction?isAjax=1&backtestId="+backtestId+"&date=2019-03-04&checkValue=right&isMobile=0&isForward=1&ajax=1"
        # u2="https://www.joinquant.com/algorithm/live/shareTransaction?isAjax=1&backtestId=b9a128cb8dba161073acffdd9fba7f7d&date=2019-03-04&checkValue=right&isMobile=0&isForward=1&ajax=1"

        # 获取网页内容
        res = requests.get(u2, cookies=self.cookies)
        res.encoding='utf-8'
        html=res.text
        soup = BeautifulSoup(html, features='lxml')
        # trs = soup.find_all('tr')
        trs = soup.find_all('tr', class_ ='\\"transaction_tr\\"')

        ntime=time.strftime("%y-%m-%d", time.localtime())
        for index in range(len(trs)):
            tr=trs[index]
            tds = tr.find_all('td')
            print(tds[0].text)
            # 获取的时间
            htmlnt=tds[1].text.replace("\\n", "").replace(" ", "");
            if ntime==htmlnt:
                print('当前的')
                print(htmlnt)
                print(tds[2].text)
                print(tds[5].text)
                print(tds[11].text)
                print (trs[index])
        # print(trs)



        # div = soup.find_all('tr')[0].find_all('td')
        # print(div[0].text)
        # print(div[1].text)
        # print(div[2].text)
        # print(div[3].text)

# border_bo position_tr

if __name__ == "__main__":
    dl = downloader()
    dl.getcookie()
    # dl.getmp3url(dl.base)
    dl.get2(dl.base)
