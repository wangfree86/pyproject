# coding=utf-8
# 例如，要导入模块 fibo 的 fib 函数，使用如下语句：
#
# >>> from fibo import fib, fib2
from GetCoin import *
from GetStock import *
from GetJianshu import *
# coding=utf-8
from bs4 import BeautifulSoup
import requests
import time
import sys
sys.path.append(r"D:\pyproject")
import constant

class getAll:
    def __init__(self):
        self.ttime11 = 0

    # 测试用的只要是指定整点就发送一次邮件
    def testsendmail(self):
        ntime = int(time.strftime("%H", time.localtime()))
        mtime = int(time.strftime("%M", time.localtime()))
        #确定多长时间发送一次
        if mtime < 110:
        # if ntime % 8 == 0 and mtime < 10:
            try:
                stock = GetStock.getAllStock(self)
            except:
                stock = 'sstock except'
            try:
                coin = GetCoin.getAllCoin(self)
            except:
                coin = 'scoin except'
            allmessage=stock+coin
            print(allmessage)
            SendMail().accesssendmail(allmessage)





    def execute1(self):
        # 一直开启的循环10分钟执行一次任务，不停止
        i = 1
        jinshu=getJianshu()
        while True:
            # 还原初始化之，每天零点还原一次
            nstr = str(i) + '循环执行中:' + '--------' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            i += 1
            print(nstr)  # 输出i


            jinshu.jianshu()
            jinshu.restoretime()

            self.testsendmail()
            time.sleep(constant.sellpnum)  # 休眠 秒


if __name__ == "__main__":

    dl = getAll()
    dl.execute1()
    # dl = GetStock()
    # dl.getAllStock()

