from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://www.joinquant.com/post/11567?f=sharelist&m=list"

url = base_url

html = urlopen(url).read().decode('utf-8')
print(html)
soup = BeautifulSoup(html, features='lxml')

div = soup.find_all('img', class_ = 'BDE_Image')

for i,each in enumerate(div):
    # if i<3:
        print(i)
        src=each.get('src')
        import requests
        r = requests.get(src)
        with open('../img/'+str(i)+'.png', 'wb') as f:
            f.write(r.content)

# print [i for i, x in enumerate(your_list) if x == 'your_item']
# your_list为待查list，your_item为具体要查的元素
# 打印出一个包含所有要查元素下标的列表

# print(BeautifulSoup(str(div[0])).find_all('img'))
# print(div[0].find_all('src'))
# print(div[1].src)
# print(soup.find('h1').get_text(), '    url: ', his[-1])