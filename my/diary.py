import docx
import os
import re

import calendar
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pyperclip
import time

import requests


# world操作
# 传入三个参数, 旧字符串, 新字符串, 文件对象7 8
def replace_text(old_text, new_text, file):
    # 遍历文件对象  33400    32647
    for f in file.paragraphs:
        # 如果 旧字符串 在 某个段落 中
        if old_text in f.text:
            print("替换前:", f.text)
            # 将段落存入 inline
            inline = f.runs
            # 遍历 段落 生成 i
            for i in inline:
                # 如果 旧字符串 在 i 中
                if old_text in i.text:
                    # 替换 i.text 内文本资源
                    text = i.text.replace(old_text, new_text)
                    i.text = text
            print("替换后===>", f.text)


def getday():
    allday = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]
    newday = datetime.datetime.now().day
    finallyday = str(allday - newday)
    return finallyday


def getweather():
    # 获取天气信息
    # base_url = "http://www.weather.com.cn/weather1d/101010100.shtml"
    base_url = "https://www.tianqi.com/beijing/"

    url = base_url

    # 添加headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    html = requests.get(url).text
    # html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    # print(html)
    # 天气
    wea = soup.find('dd', class_='weather')
    kongqi = soup.find('dd', class_='kongqi')
    kongqistr = (kongqi.h5.text + kongqi.h6.text).replace('空气质量：', '')

    weather = "天气：" + wea.span.text + "    " + kongqistr
    return weather


# 获取当前的时间，格式化我默认的格式2019年1月15日 星期二
def getNowDay():
    year = time.strftime("%Y年", time.localtime())
    m = time.strftime("%m月", time.localtime())
    if m[0] == '0':
        m = m.replace('0', '')
    d = time.strftime("%d日", time.localtime())
    if d[0] == '0':
        d = d.replace('0', '')
    week = time.strftime("%w", time.localtime())
    week = num_to_week(int(week))
    nstr = year + m + d + " " + week
    return nstr
    # nstr=time.strftime("%Y年%m月%d日  %x", time.localtime())
    # allday = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1]
    # newday = datetime.datetime.now().day
    # finallyday = str(allday - newday)
    # return finallyday


def num_to_week(num):
    numbers = {
        0: "星期日",
        1: "星期一",
        2: "星期二",
        3: "星期三",
        4: "星期四",
        5: "星期五",
        6: "星期六",
    }
    return numbers.get(num, None)


import locale

if __name__ == '__main__':

    locale.setlocale(locale.LC_CTYPE, 'chinese')
    # docx_file_name = 'C:/Users/XH/Desktop/模板.docx'
    # docx_file_name1 = 'C:/Users/XH/Desktop/模板1.docx'
    # # 获取文件对象
    # file = docx.Document(docx_file_name)
    # 三个参数: 旧的字符串, 新的字符串, 文件对象
    weather = getweather()

    day = '本月余额' + getday() + '天'

    # replace_text('天气', weather, file)
    # replace_text('本月余额', day, file)
    # file.save(docx_file_name1)

    str =getNowDay() + '\n' + weather + '\n' + day
    pyperclip.copy(str)
    getNowDay()
    # 2019年1月15日 星期二
    print("成功" + str)
    # print(docx_file_name1, "替换成功"+str)
# main()
