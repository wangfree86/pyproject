import tushare as ts

# df = ts.get_index()

df=ts.get_hist_data('159928')
df.to_csv('159928.csv')
print(df.columns.values )
print(df[['p_change','close','high']])

# df=ts.get_hist_data('159931',start='2018-01-05',end='2019-02-25')
# df.to_csv('159931.csv')
# print(df.columns.values )
# print(df[['p_change','close','high']])