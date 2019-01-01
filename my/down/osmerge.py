# -*- coding: utf-8 -*-
# Created on 2018/3/22
import os
import requests, json
import os
import time
import os

"""
下载M3U8文件里的所有片段
"""

class downloader(object):
    def __init__(self):
        self.num = 113
    # 下载ts文件
    def download(self,url, filename, download_path):
        allts = []
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
                    # 测试数据只要5片段就好
                    # allts.append(line)
                    # if len(allts):
                    # if len(allts)<2:
                      allts.append(line)

        # 0的位置是广告
        if len(allts) > 1:
            del allts[0]
            # del allts[len(allts)-1]
            for index, line in enumerate(allts):
                # if  index>51:
                    time.sleep(0.1)
                    pd_url = url.rsplit("/", 1)[0] + "/" + line
                    requests.adapters.DEFAULT_RETRIES = 5
                    res = requests.get(pd_url, timeout=3)

                    c_fule_name = str(line)
                    print(download_path + str(len(allts)) + '--' + str(index+1) + u"下载进行中"+time.strftime("%Y-%m-%d %H:%M:%S"))
                    with open(download_path + "\\" + c_fule_name, 'ab') as f:
                        f.write(res.content)
                        f.flush()
            print(download_path + u"下载完成")
            self.mergemp4(allts, filename, download_path)
            # 删除文件夹下ts
            self.deletets(download_path, allts)
        else:
            print(download_path + u"下载异常")


    # 合并文件
    # 从一个文件获取需要合并的全部ts文件名称，然后在去合并全部ts成为一个mp4文件
    def mergemp4(self,files, filename, path):
        # 合并ts文件
        os.chdir(path)
        shell_str = '+'.join(files)
        shell_str = 'copy / ' \
                    '' \
                    'b ' + shell_str + ' ' +'K:\\down\\' + filename + '.mp4'
        os.system(shell_str)
        # print(shell_str)


    def deletets(self,path, allts):
        for index, line in enumerate(allts):
            allpath = path + "\\" + line
            os.remove(allpath)


    """
    获取全部的信息，名称，和m3u8的地址
    """


    def getall(self):
        f = open('source.txt', 'r', encoding='UTF-8')
        u = f.read()
        # print(u)
        list = u.split();
        dict = {}
        key = ''
        value = ''
        for index, line in enumerate(list):
            index = index + 1
            # 奇数做key，偶数value
            if index % 2 != 0:
                key = line;
            else:
                value = line;
                dict[key] = value  # 添加
        print(dict)
        return dict


    # 创建文件夹
    def mkdir(self,path):
        folder = os.path.exists(path)

        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            # print ("---  OK  ---")

        else:
            print("---  There is this folder!  ---")

    def mainall(self,dict):
        root = 'K:\\down\\'
        ndict = dict.copy()
        for key in dict:
                # 最后的路劲
                try:
                    filename = str(self.num) + key
                    path = root + filename
                    print("总进度：" +key+ str(len(dict)) + '--' + str(self.num)+ '--' +time.strftime("%Y-%m-%d %H:%M:%S"))
                    self.mkdir(path)
                    self.download(dict[key], filename, path)
                    self.num = self.num + 1
                    time.sleep(0.1)
                    ndict.pop(key)
                except Exception as e:
                        time.sleep(9)
                        print(str(e)+"出现问题重新开始了------------------" + str(dl.num))
                        dl.mainall(ndict)

if __name__ == '__main__':
    dl = downloader()
    dict = dl.getall()
    dl.mainall(dict)


    # url="https://media-ali-oversea.wanmen.org/9cccf4a2-cfd0-4c39-9073-c033b0d2b6c1_pc_high.m3u8"
        # filename='测试名字'
        # path='D:\\testdown\\'
