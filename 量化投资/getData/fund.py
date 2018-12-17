import tushare as ts

# ts.get_hist_data('sz300001') #一次性获取全部日k线数据

df = ts.get_hist_data('300001',start='2009-10-30',end='2017-12-14')
# print(df)
#直接保存
df.to_csv('300001.csv',columns=['open','high','close','price_change','p_change'])

#选择保存
# df.to_csv('c:/day/000875.csv',columns=['date','open','high','low','close'])