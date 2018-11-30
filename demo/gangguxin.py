# coding=utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import requests
import time

import re
import requests, json


# 分享港股打新概率的的
# https://www.jisilu.cn/data/new_stock/#hkipo
# 获取json数据
# https://www.jisilu.cn/data/new_stock/hkipo/?___jsl=LST___t=1543300261298
class downloader(object):
    def __init__(self):
        self.server = 'https://www.jisilu.cn/data/new_stock/hkipo/?___jsl=LST___t=1543300261298'
        self.cookies = {}  # 初始化cookies字典变量
        self.alllist_name = []  # 存放
        self.allaction_down = []
        self.allaction_fav = []  # 存放
        self.allsongid = []  # 存放
        self.alldown = []  # 最后获取json的地址

    def get_download_url(self):
        # 添加headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        url = self.server
        print(url)
        # 获取网页内容
        html = requests.get(url, headers=headers).text
        print(html)
        html = json.loads(html)
        print(type(html))
        # html = json.dumps(html)
        # stock_cd id
        # stock_nm 名字
        # issue_price 发型价格
        # single_draw_money 一手价格
        # lucky_draw_rt 中奖概率
        # raise_money 总金额
        # total_incr_rt 总涨幅
        # gray_incr_rt 暗盘涨幅
        # first_incr_rt 开盘涨幅

        # ---------------------------------------------------------------------------------------------------------------
        # single_draw_money 一手价格
        # lucky_draw_rt 中奖概率
        # first_incr_rt 开盘涨幅
        allmoney = 0;
        number = 0;
        for f in html['rows']:
            nm = f['cell']['stock_nm']
            money = f['cell']['single_draw_money']
            lucky = f['cell']['lucky_draw_rt']
            first = f['cell']['first_incr_rt']
            if type(first) is str:
                smoney = float(money) * (float(lucky) / 100) * (float(first) / 100)
                allmoney = allmoney + smoney
                number = number + 1
                # 但个股盈利
                # print(nm + str(smoney))
                # if smoney>1000 :
                # print("大收益： "+nm + str(smoney))
                if smoney < -500:
                    print("大亏损： " + nm + str(smoney))
                    # print(html['rows'])
                    # print(html['page'])
                    # print(html['rows'][0])
                    # print(html['rows'][0]['id'])
                    # print(html['rows'][0]['cell'])
                    # print(html['rows'][0]['cell']['stock_nm'])
        print('总数量' + str(number) + '总盈利' + str(allmoney))
        print('平均获利' + str(allmoney / number))

    def test1(self):
        # 假设运气很好，每次一定中的时候
        #         总数量234总盈利152969.5789
        # 平均获利653.7161491452991
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        url = self.server
        print(url)
        # 获取网页内容
        html = requests.get(url, headers=headers).text
        print(html)
        html = json.loads(html)
        print(type(html))
        # html = json.dumps(html)
        # stock_cd id
        # stock_nm 名字
        # issue_price 发型价格
        # single_draw_money 一手价格
        # lucky_draw_rt 中奖概率
        # raise_money 总金额
        # total_incr_rt 总涨幅
        # gray_incr_rt 暗盘涨幅
        # first_incr_rt 开盘涨幅

        # ---------------------------------------------------------------------------------------------------------------
        # single_draw_money 一手价格
        # lucky_draw_rt 中奖概率
        # first_incr_rt 开盘涨幅
        allmoney = 0;
        number = 0;
        for f in html['rows']:
            nm = f['cell']['stock_nm']
            money = f['cell']['single_draw_money']
            lucky = f['cell']['lucky_draw_rt']
            first = f['cell']['first_incr_rt']
            if type(first) is str:
                smoney = float(money) * (float(first) / 100)
                allmoney = allmoney + smoney
                number = number + 1
                # 但个股盈利
                # print(nm + str(smoney))
                if smoney > 1000:
                    print("大收益： " + nm + str(smoney))
                if smoney < -1000:
                    print("大亏损： -------" + nm + str(smoney))
                    # print(html['rows'])
                    # print(html['page'])
                    # print(html['rows'][0])
                    # print(html['rows'][0]['id'])
                    # print(html['rows'][0]['cell'])
                    # print(html['rows'][0]['cell']['stock_nm'])
        print('总数量' + str(number) + '总盈利' + str(allmoney))
        print('平均获利' + str(allmoney / number))

    def test2(self):
        # 添加headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
        url = self.server
        print(url)
        # 获取网页内容
        html = requests.get(url, headers=headers).text
        print(html)
        html = json.loads(html)
        print(type(html))
        # html = json.dumps(html)
        # stock_cd id
        # stock_nm 名字
        # issue_price 发型价格
        # single_draw_money 一手价格
        # lucky_draw_rt 中奖概率
        # raise_money 总金额
        # total_incr_rt 总涨幅
        # gray_incr_rt 暗盘涨幅
        # first_incr_rt 开盘涨幅

        # ---------------------------------------------------------------------------------------------------------------
        # single_draw_money 一手价格
        # lucky_draw_rt 中奖概率
        # first_incr_rt 开盘涨幅
        # 01183
        allmoney = 0;
        number = 0;
        for f in html['rows']:
            stock_cd = f['cell']['stock_cd']
            list_dt2 = f['cell']['list_dt2']
            nm = f['cell']['stock_nm']
            money = f['cell']['single_draw_money']
            lucky = f['cell']['lucky_draw_rt']
            first = f['cell']['first_incr_rt']
            raise_money = f['cell']['raise_money']
            # if stock_cd=='01183':
            #     break

            year=list_dt2.split('-')[0]
            if year=='2017':
                if type(first) is str:
                    if float(raise_money) < 8:
                        smoney = float(money) * (float(lucky) / 100) * (float(first) / 100)
                        allmoney = allmoney + smoney
                        number = number + 1
                        # 但个股盈利
                        # print(nm + str(smoney))
                        if smoney > 1000:
                            print("大收益： " + nm + str(smoney))
                        if smoney < -1000:
                            print("大亏损： " + nm + str(smoney))
                            # print(html['rows'])
                            # print(html['page'])
                            # print(html['rows'][0])
                            # print(html['rows'][0]['id'])
                            # print(html['rows'][0]['cell'])
                            # print(html['rows'][0]['cell']['stock_nm'])
        print('总数量' + str(number) + '总盈利' + str(allmoney))
        print('平均获利' + str(allmoney / number))


if __name__ == "__main__":
    # lucky='100.00'
    # first='1.43'
    # m='100'
    # smoney = float(m) * (float(lucky) / 100) * (float(first) / 100)
    # # al = 2800.00 * (100.00 / 100) * (3.5 / 100)
    # print(smoney)
    dl = downloader()
    dl.test2()
    # str ='2018-05-04';
    # ii=str.split('-')[0]
    # print(ii)

    # 1.根据真实中签概率
    # 每次打新都买盈利情况  盈利=一手资金*概率*首日涨幅
    # 总数量234总盈利42948.289083350006
    # 平均获利183.5396969373932


    # 2.假设运气很好，每次一定中的时候
    # 总数量234总盈利152969.5789
    # 平均获利653.7161491452991

    # 3.优化策略不申购资金大于8亿的股票
    # 总数量188总盈利41642.02305135001
# 平均获利221.50012261356386

# 3.优化策略不申购资金大于1亿的股票
# 总数量188总盈利41642.02305135001
# 平均获利221.50012261356386
