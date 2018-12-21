# -*- coding: utf-8 -*-
# Created on 2018/3/22
import os
import requests, json

"""
获取全部的信息，名称，和m3u8的地址
"""
def getall():
    f = open('source.txt','r', encoding='UTF-8')
    u = f.read()
    # print(u)
    list=u.split('\n');
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

import os

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
        npath=root+str(num)+key
        print(npath)
        mkdir(npath)
        num=num+1
     # print (key+'-----'+dict[key])
