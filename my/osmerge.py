# -*- coding: utf-8 -*-
# Created on 2018/3/22
import os
import requests, json
import os
"""
下载M3U8文件里的所有片段
"""

# 下载ts文件
def download(url,filename,download_path):
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
                allts.append(line)
    for index, line in enumerate(allts):
        pd_url = url.rsplit("/", 1)[0] + "/" + line
        # print(pd_url)
        res = requests.get(pd_url)
        c_fule_name = str(line)
        with open(download_path + "\\" + c_fule_name, 'ab') as f:
            f.write(res.content)
            f.flush()
    mergemp4(allts,filename,download_path)
    print(u"下载完成")


# 合并文件
# 从一个文件获取需要合并的全部ts文件名称，然后在去合并全部ts成为一个mp4文件
def mergemp4(files,filename,path):
        # 合并ts文件
    os.chdir(path)
    shell_str = '+'.join(files)
    shell_str = 'copy /b '+ shell_str +' '+path+ filename+'.mp4'
    print(shell_str)
    os.system(shell_str)
    print(shell_str)

"""
获取全部的信息，名称，和m3u8的地址
"""
def getall():
    f = open('source.txt','r', encoding='UTF-8')
    u = f.read()
    # print(u)
    list=u.split( );
    dict = {}
    key=''
    value=''
    for index, line in enumerate(list):
        index=index+1
        # 奇数做key，偶数value
        if index%2!=0 :
            key=line;
        else :
            value=line;
            dict[key] =value # 添加
    print(dict)
    return dict
# 创建文件夹
def mkdir(path):

    folder = os.path.exists(path)

    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        # print ("---  OK  ---")

    else:
        print( "---  There is this folder!  ---")
if __name__ == '__main__':
    root='D:\\testdown\\'
    dict=getall()
    num=0
    for key in dict:
        # 最后的路劲
        filename=str(num)+key
        path=root+filename
        print(path)
        mkdir(path)
        download(dict[key],filename,path)
        num=num+1

    # url="https://media-ali-oversea.wanmen.org/9cccf4a2-cfd0-4c39-9073-c033b0d2b6c1_pc_high.m3u8"
        # filename='测试名字'
        # path='D:\\testdown\\'
