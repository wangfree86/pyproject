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

    def getcookie(self):
        f = open(r'test.txt', 'r')  # 打开所保存的cookies内容文件
        for line in f.read().split(';'):  # 按照字符：进行划分读取
            # 其设置为1就会把字符串拆分成2份
            name, value = line.strip().split('=', 1)
            self.cookies[name] = value  # 为字典cookies添加内容

    def get_download_url(self):
        url = self.server
        print(url)
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
    dl.getcookie()
    dl.get_download_url()
    print(dl.alllist_name)
    print(dl.allaction_down)
    print(dl.allaction_fav)
    print(dl.allsongid)
    nowtiem = str(int(round(time.time() * 1000)))
    for i, item in enumerate(dl.allsongid):
        type = dl.allaction_fav[i]
        str = dl.down % (nowtiem, item, type, nowtiem)
        dl.alldown.append(str)
        dl.getmp3url(str)
        # print(str)
    print(dl.alldown)



    # alllist_name
    # ['游牧民族', '镇魂-死生关', '付春风', '棠梨煎雪（cover银临）', '待字闺中', '《破天哥哥保护你》——第二口水妹的九阴江湖见闻录二', '风云叹（献给《傲风》）', '社戏', '【魔兽】亡灵序曲（玄觞LIVE版）', '【玄舞花下】⑧云梦传奇—第二口水妹九阴江湖见闻录五', '《乱世九阴》——第二口水妹的九阴江湖见闻录', '《再见江湖》——第二口水妹九阴江湖见闻录四', '墨宝·妻书', '【玄舞花下】⑥《空待》ft.王朝', '「星·弦」——玄觞专辑《心弦》①', '天神系列3：【世纪对唱】冰凉拥抱', '「召唤王妃」——玄觞专辑《心弦》②', '「遇见你」——玄觞专辑《心弦》⑤', '绿衣 FT.小爱的妈', '墨宝·小小侠客']
    # allaction_down
    #  ['http://5sing.kugou.com/yc/down/3676331', 'http://5sing.kugou.com/yc/down/3666882', 'http://5sing.kugou.com/yc/down/3651857', 'http://5sing.kugou.com/fc/down/16570917', 'http://5sing.kugou.com/yc/down/3608486', 'http://5sing.kugou.com/yc/down/1326550', 'http://5sing.kugou.com/fc/down/3258372', 'http://5sing.kugou.com/fc/down/7013533', 'http://5sing.kugou.com/fc/down/5308966', 'http://5sing.kugou.com/yc/down/2000961', 'http://5sing.kugou.com/yc/down/1174991', 'http://5sing.kugou.com/fc/down/8541920', 'http://5sing.kugou.com/yc/down/426403', 'http://5sing.kugou.com/yc/down/2241679', 'http://5sing.kugou.com/yc/down/2296144', 'http://5sing.kugou.com/yc/down/1846740', 'http://5sing.kugou.com/yc/down/2208666', 'http://5sing.kugou.com/yc/down/3140169', 'http://5sing.kugou.com/fc/down/2924768', 'http://5sing.kugou.com/yc/down/1692309']
    # allaction_fav
    # ['1', '1', '1', '2', '1', '1', '2', '2', '2', '1', '1', '2', '1', '1', '1', '1', '1', '1', '2', '1']
    # allsongid
    # ['3676331', '3666882', '3651857', '16570917', '3608486', '1326550', '3258372', '7013533', '5308966', '2000961', '1174991', '8541920', '426403', '2241679', '2296144', '1846740', '2208666', '3140169', '2924768', '1692309']
    # print(html.get('data').get('songName'))
    # 游牧民族
    # print(html.get('data').get('authorName'))
    # 小玄子
    # print(html.get('data').get('fileName'))
    # http://data.5sing.kgimg.com/G091/M08/1E/14/O5QEAFtsU2eAERf0AJCgfbeR7nk600.mp3
    #     dl.alldown
    # http://service.5sing.kugou.com/song/getPermission?jsoncallback=jQuery17036960075558330574_1536894741712&songId=3676331&songType=1&_=1536894741712
