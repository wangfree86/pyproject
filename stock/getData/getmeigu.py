#python
import json,urllib
import requests
import re
import csv
import time
# 获取美股的数据，但是这个接口数据不足，历史数据太少。
# https://www.nowapi.com/api/finance.stock_realtime
# https://uqer.io/data/search/%E7%BE%8E%E8%82%A1
codename='gb_sqqq'
url = 'http://api.k780.com'
data = {
    'app' : 'finance.stock_realtime',
    'symbol' : codename,
    'appkey' : '10003',
    'sign' : 'b59bc3ef6191eb9f747dd4e83c99f2a4',
    'format' : 'json',
}

# get请求
# https://www.jianshu.com/u/5b4978fe1f2a?order_by=shared_at&page=2
html = requests.get(url,  params=data).text
a_result = json.loads(html)
print(a_result)

if a_result:
    if a_result['success'] != '0':
        # print (a_result['result']['lists'])
        print (a_result['result']['lists'][codename]['sname'])
        print (a_result['result']['lists'][codename]['last_price']+'美金')
        print (a_result['result']['lists'][codename]['mvalue']+'美金')
        print (a_result['result']['lists'][codename]['rise_fall_per']+'%')
        print (a_result['result']['lists'][codename]['uptime'])
    else:
        print (a_result['msgid']+' '+a_result['msg'])
else:
    print ('Request nowapi fail.')
