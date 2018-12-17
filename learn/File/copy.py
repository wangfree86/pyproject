import requests, json
import os, base64


class downloader(object):
    def __init__(self):
        self.server = 'http://5sing.kugou.com/xuanshang/default.html'


def switch(sourcestr,targetstr):
    source = open(sourcestr, 'r')
    f1 = json.loads(source.read())
    code = f1['policyCode']
    # source.close()


    signList = f1['signList'][0]['viewData'][0]
    promptList = f1['promptList'][0]['signData'][0]


    target = open(targetstr, 'r')
    f2 = json.loads(target.read())
    code = f2['policyCode']
    print(code)
    p2 = f2['signList'][0]['viewData'][0]

    f2['signList'][0]['viewData'][0] = signList
    f2['promptList'][0]['signData'][0] = promptList

    print(f2)
    print(f2['signList'][0]['viewData'][0])

    savefile(targetstr,f2)

def savefile(url,content):
    content = json.dumps(content)

    # print(content)
    # file = open(url, 'wrb')
    # # file.truncate();
    # file.write('hello')
    # file.close()

    # url1='C:/test1/copy/18112910592056511111.txt'
    file = open(url, 'w')
    file.write(content)
    file.close()




def getall(file_dir):
    for root, dirs, files in os.walk(file_dir):
        source=''
        target=''
        for f in files:
            # 获取2个文件，短名称的要字段copy到长名称中
            if len(f)<12:
                source=file_dir+f
            else :
                target=file_dir+f
        switch(source,target)

if __name__ == "__main__":
    dl = downloader()
    root='C:/copy/'
    getall(root)

    # url1='C:/test1/copy/181129105920565.txt'
    # file = open(url1, 'w')
    # # file.truncate();
    # file.write('hello')
    # file.close()
