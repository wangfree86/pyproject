# -*- coding: utf-8 -*-
# Created on 2018/3/22
import os
import requests, json

"""
下载M3U8文件里的所有片段
"""


def download(url):
    allts = []
    download_path = os.getcwd() + "\download"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    all_content = requests.get(url).text  # 获取M3U8的文件内容
    file_line = all_content.split("\n")  # 读取文件里的每一行
    # 通过判断文件头来确定是否是M3U8文件
    if file_line[0] != "#EXTM3U":
        raise BaseException(u"非M3U8的链接")
    else:
        for index, line in enumerate(file_line):
            if ".ts" in line:
                allts.append(line)

    for index, line in enumerate(allts):

        pd_url = url.rsplit("/", 1)[0] + "/" + line
        # print(pd_url)
        res = requests.get(pd_url)
        c_fule_name = str(line)
        with open(download_path + "\\" + c_fule_name, 'ab') as f:
            f.write(res.content)
            f.flush()
    print(u"下载完成")


if __name__ == '__main__':
    download(
        "https://media-ali-oversea.wanmen.org/9cccf4a2-cfd0-4c39-9073-c033b0d2b6c1_pc_high.m3u8")
