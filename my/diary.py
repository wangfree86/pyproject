import docx
import os
import re

import calendar
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
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
    finallyday=str(allday - newday)
    return finallyday
def getweather():
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
    weather="天气："+wea[0].text+"    "+tem[1].span.text+'-'+tem[0].text
    weather=weather.replace("\n", "")
    return weather

if __name__ == '__main__':
    docx_file_name = 'C:/Users/XH/Desktop/模板.docx'
    docx_file_name1 = 'C:/Users/XH/Desktop/模板1.docx'
    # 获取文件对象
    file = docx.Document(docx_file_name)
    # 三个参数: 旧的字符串, 新的字符串, 文件对象
    replace_text('天气', getweather(), file)
    day='本月余额'+ getday()+'天'
    replace_text('本月余额',day, file)
    file.save(docx_file_name1)
    print(docx_file_name1, "替换成功")
    # main()
