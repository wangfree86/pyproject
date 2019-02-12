from urllib.request import urlopen, Request
import json
import time
class GetCoin:

    def getAllCoin(self):
        # ===binance交易所，获取全部24小时内的数据
        # fopen = open('tt.txt', 'r')
        # content = fopen.readlines()
        # print(content[0])
        #   a_result = json.loads(content[0])
        url = 'https://api.binance.com/api/v1/ticker/24hr'  # tick数据

        # 抓取数据，带有浏览器伪装
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        request = Request(url=url, headers=headers)
        content = urlopen(request, timeout=15).read()
        content = content.decode('utf-8')
        #
        # print(content)



        watchCoin = {'BTCUSDT','ETHUSDT','EOSUSDT'}

        a_result = json.loads(content)
        i=0
        allcoin=''
        for coins in a_result:
            # print(coins)
            if coins.get("symbol") in watchCoin:
                i=i+1

                #转换成localtime
                time_local = time.localtime(coins.get("openTime")/1000)
                #转换成新的时间格式(2016-05-05 20:28:54)
                nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
                newstr='币：'+coins.get("symbol")+' ：'+coins.get("priceChangePercent")+'%    '\
                       +coins.get("lastPrice")+'美金   时间：'+nowtime
                allcoin=allcoin+"\n"+newstr
                print(newstr)
        return allcoin
        print(allcoin)
                # print(coins)
