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
        self.server = 'https://www.jisilu.cn/data/new_stock/hkipo/?___jsl=LST___t=1543300261298'
        self.down = 'http://service.5sing.kugou.com/song/getPermission?jsoncallback=jQuery17036960075558330574_%s&songId=%s&songType=%s&_=%s'
        self.cookies = {}  # 初始化cookies字典变量
        self.alllist_name = []  # 存放
        self.allaction_down = []
        self.allaction_fav = []  # 存放
        self.allsongid = []  # 存放
        self.alldown = []  # 最后获取json的地址

    def getcookie(self):
        f = open(r'test.txt', 'r')  # 打开所保存的cookies内容文件
        for line in f.read().split(';'):  # 按照字符：进行划分读取
            # 其设置为1就会把字符串拆分成2份
            name, value = line.strip().split('=', 1)
            self.cookies[name] = value  # 为字典cookies添加内容

    def get_download_url(self):
        # 添加headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        url = self.server
        print(url)
        # 获取网页内容
        html = requests.get(url, headers=headers).text
        print(html)
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




if __name__ == "__main__":
    dl = downloader()
    dl.getcookie()
    dl.get_download_url()
    # print(dl.alllist_name)
    # print(dl.allaction_down)
    # print(dl.allaction_fav)
    # print(dl.allsongid)
    # nowtiem = str(int(round(time.time() * 1000)))
    # for i, item in enumerate(dl.allsongid):
    #     type = dl.allaction_fav[i]
    #     str = dl.down % (nowtiem, item, type, nowtiem)
    #     dl.alldown.append(str)
    #     dl.getmp3url(str)
    #     # print(str)
    # print(dl.alldown)
