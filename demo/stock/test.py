

import tushare as ts

df=ts.get_hist_data('sz') #一次性获取全部日k线数据

df.to_csv('c:/day/sz.csv')

print(df)

# for dd in df:
#         print(dd)
#         print(dd.date)
        # film_dict = {}
        # title=tex.find('a', class_='title')
        # if not title is None:




# import time
# import datetime
# #今天星期几
# print (time.strftime("%w"))
# today=int(time.strftime("%w"))
# print (today)
# #某个日期星期几
# anyday=datetime.datetime(2013,5,13).strftime("%w")
# print (time)



# import tushare as ts
#
# df=ts.get_hs300s()
# df.to_csv('c:/day/000875.csv')
# print(ts.get_hs300s())


# df = ts.get_hist_data('000875')
# #直接保存
# df.to_csv('c:/day/000875.csv')

#选择保存
# df.to_csv('c:/day/000875.csv',columns=['open','high','low','close'])