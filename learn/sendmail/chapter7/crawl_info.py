from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import requests


def get_info(url):
    name = ''
    print(url)
    # 获取网页内容
    html = requests.get(url).text
    # 获取网页元素
    soup = BeautifulSoup(html, 'lxml')
    # 根据条件筛选元素
    img_ul = soup.find_all('img', class_="BDE_Image")
    for i, each in enumerate(img_ul):
        src = each.get('src')
        print(src)
        name = name +'\n'+ src
    return name
