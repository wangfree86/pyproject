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
        self.server = 'http://5sing.kugou.com/xuanshang/default.html'
        self.down = 'http://service.5sing.kugou.com/song/getPermission?jsoncallback=jQuery17036960075558330574_%s&songId=%s&songType=%s&_=%s'
        self.cookies = {}  # 初始化cookies字典变量
        self.alllist_name = []  # 存放
        self.allaction_down = []
        self.allaction_fav = []  # 存放
        self.allsongid = []  # 存放
        self.alldown = []  # 最后获取json的地址

        self.useurl = []

    def getcookie(self):
        f = open(r'test.txt', 'r')  # 打开所保存的cookies内容文件
        for line in f.read().split(';'):  # 按照字符：进行划分读取
            # 其设置为1就会把字符串拆分成2份
            name, value = line.strip().split('=', 1)
            self.cookies[name] = value  # 为字典cookies添加内容

    def get_download_url(self):
        url = self.server
        # 获取网页内容
        html = requests.get(url).text
        # 获取网页元素
        soup = BeautifulSoup(html, 'lxml')
        # 根据条件筛选元素
        div = soup.find_all('div', class_="song_list")
        for divitem in div:
            liall = divitem.find_all('li')

            for a, alleach in enumerate(liall):
                list_name = alleach.find('strong', class_="lt list_name").find('a').get('title')
                # a = BeautifulSoup(list_name, 'lxml').find_all('a')
                action_down = alleach.find('a', class_="action_down").get('href')
                action_fav = alleach.find('a', class_="action_fav").get('songkind')
                songid = alleach.find('a', class_="action_fav").get('songid')
                self.alllist_name.append(list_name)
                self.allaction_down.append(action_down)
                self.allaction_fav.append(action_fav)
                self.allsongid.append(songid)

                # 获取MP3具体下载地址

    def get_alluser(self, url):
        html = requests.get(url).text
        # 获取网页元素
        soup = BeautifulSoup(html, 'lxml')
        # 根据条件筛选元素
        a = soup.find_all('a', class_="show_userCard_link")
        number = soup.find('id', id="totalfans")
        ss=number.find('a')
        print(ss.text)
        # for item in a:
        #     href = item.get('href')
        #     self.useurl.append(href)
        # nowint=len(self.useurl)
        # print(nowint)
        # if(nowint<22):
        #     for i, item in enumerate(self.useurl):
        #         self.get_alluser(self.useurl[i])
        # else:
        #         print(len(self.useurl))
        #         print(self.useurl)
        #         print("停止")



    def getmp3url(self, str):
        # 获取网页内容
        res = requests.get(str, cookies=self.cookies).text
        tt = re.findall(r"{.*}", res)[0]
        # 最后解析的json了
        html = json.loads(tt)
        # print(html.get('data').get('songName'))
        # print(html.get('data').get('authorName'))
        # print(html.get('data').get('fileName'))
        name = html.get('data').get('songName') + "-" + html.get('data').get('authorName')
        url = html.get('data').get('fileName')
        print(name + "开始下载")
        r = requests.get(url)
        with open('../img/' + name + '.mp3', 'wb') as f:
            f.write(r.content)
        print(name + "完成下载")


if __name__ == "__main__":
    dl = downloader()
    dl.get_alluser(dl.server)
    print("完成停止")
    # for i, item in enumerate(dl.useurl):
    # print(dl.useurl)
    # dl.getcookie()
    # dl.get_download_url()
    # nowtiem = str(int(round(time.time() * 1000)))
    # for i, item in enumerate(dl.allsongid):
    #     type = dl.allaction_fav[i]
    #     str = dl.down % (nowtiem, item, type, nowtiem)
    #     dl.alldown.append(str)
    #     dl.getmp3url(str)
    #     # print(str)
    # print(dl.alldown)
