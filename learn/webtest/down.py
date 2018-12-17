# coding=utf-8
import requests
url="http://data.5sing.kgimg.com/G130/M00/08/13/IocBAFsjigyAdIgJAJTR2PErb7E950.mp3"
print("开始")
r = requests.get(url, stream=True)    # stream loading
# mode=
# w        打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb       （多了一个二进制格式） 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
with open('../img/image3.mp3', 'wb') as f:
    # for 这行代码是可选的，如果选择了，通过chunk_size控制每一次下载多少 chunk_size 单位是b 所以一般用 1024=1k也不错了。
    # 如果没for chunk in r.iter_content(chunk_size=1024):所有下载内容保存到内容中下载完成才会写入硬盘，几百兆的电影就无法下载了
    for chunk in r.iter_content(chunk_size=1024):
        f.write(chunk)