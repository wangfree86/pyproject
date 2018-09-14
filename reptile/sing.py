from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import requests
import time

class downloader(object):
    def __init__(self):
        self.server = 'http://5sing.kugou.com/xuanshang/default.html'
        self.down = 'http://service.5sing.kugou.com/song/getPermission?jsoncallback=jQuery17036960075558330574_%s&songId=%s&songType=%s&_=%s'
        self.alllist_name = []          #存放
        self.allaction_down = []          #存放
        self.allaction_fav = []          #存放
        self.allsongid = []          #存放
        self.alldown = []

    def get_download_url(self):
        url=self.server
        print(url)
        # 获取网页内容
        html = requests.get(url).text
        # 获取网页元素
        soup = BeautifulSoup(html, 'lxml')
        # 根据条件筛选元素
        div = soup.find_all('div', class_ ="song_list")
        for divitem in div:
            liall = divitem.find_all('li')

            for a,alleach in enumerate(liall):
                list_name =alleach.find('strong', class_ ="lt list_name").find('a').get('title')
                # a = BeautifulSoup(list_name, 'lxml').find_all('a')
                action_down =alleach.find('a', class_ ="action_down").get('href')
                action_fav =alleach.find('a', class_ ="action_fav").get('songkind')
                songid =alleach.find('a', class_ ="action_fav").get('songid')
                self.alllist_name.append(list_name)
                self.allaction_down.append(action_down)
                self.allaction_fav.append(action_fav)
                self.allsongid.append(songid)




if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print(dl.alllist_name)
    print(dl.allaction_down)
    # 类型1,2
    print(dl.allaction_fav)
    print(dl.allsongid)
    nowtiem=str(int(round(time.time() * 1000)))
    for i,item in enumerate(dl.allsongid):

       type=dl.allaction_fav[i]
       str =dl.down %(nowtiem,item,type,nowtiem)
       dl.alldown.append(str)
       print(str)
    print(dl.alldown)
    # for n in range(1, dl.all+1):
    #     n=str(n)
    #
    #     print("当前页码"+n)
    #
    # print("总src量"+str(dl.name))

