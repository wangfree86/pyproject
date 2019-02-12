from urllib.request import urlopen, Request
import json
import json, urllib
import requests

import sys
sys.path.append(r"D:\pyproject")
import constant
class GetStock:
    def __init__(self):
        self.uptime = "00"
    def setuptime(self,time):
        self.uptime = time

    def num_to_week(self,num):
        numbers = {
            'gb_sqqq': "纳指3倍空",
            'gb_chau': "a股2倍多",
            'gb_ugld': "黄金3倍多",
            'gb_vnm': "越南",
            'gb_ewt': "台湾",
            'gb_scif': "印度小盘"
            # 'gb_sqqq': "星期六",
        }
        return numbers.get(num, None)

    def getAllStock(self):
        # allstock = ['gb_sqqq']
        allstock = ['gb_sqqq', 'gb_chau', 'gb_ugld', 'gb_vnm', 'gb_ewt', 'gb_scif']
        allstr = ''
        stock=GetStock()
        for name in allstock:
            s = stock.getStock(name)
            allstr = allstr + '\n' + s

        allstr=allstr+ '\n'+stock.uptime
        print(allstr)
        return allstr

    def getStock(self, codename):
        # 获取美股的数据，但是这个接口数据不足，历史数据太少。
        # https://www.nowapi.com/api/finance.stock_realtime
        # https://uqer.io/data/search/%E7%BE%8E%E8%82%A1

        url = 'http://api.k780.com'
        data = {
            'app': 'finance.stock_realtime',
            'symbol': codename,
            'appkey': constant.appkey,
            'sign': constant.sign,
            'format': 'json',
        }

        # get请求
        # https://www.jianshu.com/u/5b4978fe1f2a?order_by=shared_at&page=2
        html = requests.get(url, params=data).text
        a_result = json.loads(html)
        # print(a_result)
        newstr = ''
        newtime=''
        if a_result:
            if a_result['success'] != '0':
                # print (a_result['result']['lists'])symbol
                stock = a_result['result']['lists'][codename]
                newstr =self.num_to_week(stock['symbol']) + ' ' + stock['rise_fall_per']+'% ' + stock['last_price']+"美金"
                self.uptime=stock['uptime']
                print(newstr)
            else:
                print(a_result['msgid'] + ' ' + a_result['msg'])
        else:
            print('Request nowapi fail.')
        return newstr

