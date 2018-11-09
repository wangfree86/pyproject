from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
# 获取天气信息
base_url = "http://www.weather.com.cn/weather1d/101010100.shtml"

url = base_url

html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

# 天气
wea = soup.find_all('p', class_='wea')
# 温度，0是最高，1是最低
tem = soup.find_all('p', class_='tem')
# 日出时间
sun = soup.find('p', class_='sun sunUp')
print(wea[0].text)
print(tem[0].span.text)
print(tem[1].span.text)
print(sun.span.text)
# print(zs)


# print [i for i, x in enumerate(your_list) if x == 'your_item']
# your_list为待查list，your_item为具体要查的元素
# 打印出一个包含所有要查元素下标的列表

# print(BeautifulSoup(str(div[0])).find_all('img'))
# print(div[0].find_all('src'))
# print(div[1].src)
# print(soup.find('h1').get_text(), '    url: ', his[-1])
