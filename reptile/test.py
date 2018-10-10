# coding=utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import requests
import time

import re
import requests, json

import requests
import re
import csv
import time


class downloader(object):
    def __init__(self):
        self.server = 'https://www.jianshu.com/u/5b4978fe1f2a'
        self.allsongid = []  # 存放
        self.page = 1

    def get_download_url(self):
        url = self.server
        # print(url)

        # 添加headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        # 添加get，pos参数
        data = {'order_by': 'shared_at',
                'page': self.page,
                }
        # get请求
        # https://www.jianshu.com/u/5b4978fe1f2a?order_by=shared_at&page=2
        html = requests.get(url, headers=headers, params=data).text
        # pst请求
        # html = requests.post(url, headers=headers, params=data).text
        # 获取网页内容
        # print(html)
        # 获取网页元素
        soup = BeautifulSoup(html, 'lxml')
        # 根据条件筛选元素
        soup1 = soup.find('div', class_='col-xs-16 main')
        texs = soup1.find_all('a', class_="title")
        for tex in texs:
            self.allsongid.append(tex.text)
            # print(tex.text)
        # print(self.allsongid)
        self.save_infor(self.allsongid)
        time.sleep(1)
        self.page = self.page + 1
        self.get_download_url()

    def save_infor(self, one_page_film):
        # print("-------")
        print(one_page_film)

        with open('name1.csv', 'a', newline='', errors='ignore') as f:
            csv_file = csv.writer(f)
            for one in one_page_film:
                csv_file.writerow([one, ""])


if __name__ == "__main__":
    obj = None
    if obj is None:
        print('a is not empty')
    else:
        print('qqqq')
# dl = downloader()
# dl.page+= 11
# if 1>0:
#     print(dl.page)
# dl.get_download_url()
# save_infor(dl.allsongid)
