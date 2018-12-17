import requests, json
import os, base64


class downloader(object):
    def __init__(self):
        self.server = 'http://5sing.kugou.com/xuanshang/default.html'


def get_pic(url,name):
    print(url)
    f = open(url, 'r')
    # f = open('C:/test1/181129105920565.txt', 'r')
    f1 = json.loads(f.read())
    code = f1['policyCode']
    p1name=f1['agentres'][0]['name']
    p1name=f1['agentres'][0]['name']
    print(p1name)
    # print(f1['currInsureType'])
    # print(f1['policyCode'])
    # print(f1['signList'])
    # # 签名3-5个
    p1 = f1['signList'][0]['src'][0].split('data:image/png;base64,')[1]
    p2 = f1['signList'][0]['src'][1].split('data:image/png;base64,')[1]
    p3 = f1['signList'][0]['src'][2].split('data:image/png;base64,')[1]
    save(p1, code + '-'+name+'p1')
    # save(p1, code + '-'+name+'-'+p1name+'p1')
    save(p2, code + '-'+name+'p2')
    save(p3, code + '-'+name+'p3')
    # print(f1['signList'][0])
    if len(f1['signList'][0]['src']) == 4:
        p4 = f1['signList'][0]['src'][3].split('data:image/png;base64,')[1]
        save(p4, code + '-'+name+'p4')
    if len(f1['signList'][0]['src']) == 5:
        p4 = f1['signList'][0]['src'][3].split('data:image/png;base64,')[1]
        save(p4, code + '-'+name+'p4')
        p5 = f1['signList'][0]['src'][4].split('data:image/png;base64,')[1]
        save(p5, code + '-'+name+'p5')

    # print(f1['signList'][0]['src'][0])
    # print(f1['signList'][0]['src'][1])
    # print(f1['signList'][0]['src'][2])


    # print(f1['signList'][0]['src'])
    # print(f1['signList'][0]['src'][0])
    # print(f1['signList'][0]['src'][1])
    # print(f1['signList'][0]['src'][2])
    # # print(f1['signList'][0]['src'][3])
    #
    # # 签名2个
    # print(f1['promptList'])
    # print(f1['promptList'][0]['src'][0])

    pp1 = f1['promptList'][0]['src'][0].split('data:image/png;base64,')[1]
    save(pp1, code + '-'+name+'pp1')
    if len(f1['promptList'][0]['src']) == 2:
        pp2 = f1['promptList'][0]['src'][1].split('data:image/png;base64,')[1]
        save(pp2, code + '-'+name+'pp2')


    # print(p1)
    # pic1=p1.split('data:image/png;base64,')[1]
    # print(pic1)
    # save(pic1,code+'pic1')


def save(pic1, name):
    imgdata = base64.b64decode(pic1)
    file = open('C:/test1/t/' + name + '.png', 'wb')
    file.write(imgdata)
    file.close()

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(files) #当前路径下
        for f in files:
            url='C:/test1/source/'+f
            name=f.split('.')[0]
            # print(f.split('.')[0])
            get_pic(url,name)
if __name__ == "__main__":
    dl = downloader()
    root='C:/test1/source'
    file_name(root)
    # url = 'C:/test1/181129105920565.txt'
    # get_pic(url)
