# -*- coding: utf-8 -*-
# Created on 2018/3/22
import os
import requests, json
import os
"""
下载M3U8文件里的所有片段
"""


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
    print(u"下载完成")

# 合并文件
# 从一个文件获取需要合并的全部ts文件名称，然后在去合并全部ts成为一个mp4文件
def mergemp4(m3u8name,filename,path):
    #exec_str = r'copy /b  ts/c9645620628078.ts+ts/c9645620628079.ts  ts/1.ts'
    #os.system(exec_str)
    f = open(m3u8name, 'r', encoding='utf-8')
    text_list = f.readlines()
    files = []
    for i in text_list:
        if i.find('#EX')==-1:
            files.append(i)

    f.close()


    tmp = []
    for file in files[0:450]:
        tmp.append(file.replace("\n",""))
        # 合并ts文件
    os.chdir(path)
    shell_str = '+'.join(tmp)
    shell_str = 'copy /b '+ shell_str + filename+'.mp4'
    print(shell_str)
    os.system(shell_str)
    print(shell_str)


if __name__ == '__main__':
    url="https://media-ali-oversea.wanmen.org/9cccf4a2-cfd0-4c39-9073-c033b0d2b6c1_pc_high.m3u8"
    filename='测试名字'
    path='D:\\testdown'
    download(url,filename,path)
