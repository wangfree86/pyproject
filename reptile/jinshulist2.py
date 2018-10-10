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


# 获取简书专栏的测试，区块链研习社的测试
# 1.需要添加header针对简单的反爬虫
# 2.保存到cvs
# 3.类内部调用的函数默认都会有一个默认self，需要注意
# 4.每次休息0.1秒，9800篇文章，预计1.5分钟+完成，
class downloader(object):
    def __init__(self):
        self.base = 'https://www.jianshu.com'
        self.server = 'https://www.jianshu.com/c/b17f09dc2831'
        self.allmessage = []  # 存放
        self.page = 201

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
        soup1 = soup.find('div', class_='col-xs-24 col-sm-16 main')
        divs = soup1.find_all('div', class_="content")
        for tex in divs:
            film_dict = {}
            title=tex.find('a', class_='title')
            if not title is None:
                film_dict['name'] = tex.find('a', class_='title').text
                film_dict['href'] = tex.find('a', class_='title').get('href')

                film_dict['nickname'] = tex.find_all('a')[1].text
                film_dict['comments'] = tex.find_all('a')[2].text
                sapn1=tex.find_all('span')
                if len(sapn1)>0:
                    film_dict['like'] = tex.find_all('span')[0].text
                self.allmessage.append(film_dict)
            else:
                print("---")
        print(self.page)
        print(len(self.allmessage))
        print(self.allmessage)
        if len(self.allmessage)>1:
            self.save_infor(self.allmessage)
            self.allmessage.clear()
            time.sleep(0.1)
            self.page+= 1
            self.get_download_url()

    def save_infor(self, one_page_film):
        with open('newlist1.csv', 'a', newline='', errors='ignore') as f:
            csv_file = csv.writer(f)
            for one in one_page_film:
                csv_file.writerow(
                        [one['name'], self.base + one['href'], one['nickname'], one['comments'],
                         one['like']])

    def setheader(self):
        headers = ['name', 'href', 'nickname', 'comments', 'like']
        with open('newlist1.csv', 'a', newline='', errors='ignore') as f:
            csv_file = csv.writer(f)
            csv_file.writerow(headers)


if __name__ == "__main__":
    dl = downloader()
    dl.setheader()
    dl.get_download_url()
    # save_infor(dl.allmessage)
