import tushare as ts

df = ts.get_index()
print(df)
# aqicsv[aqicsv["predictaqi_norm1"]>100]
# aqicsv[(aqicsv["FID"]>37898) & (aqicsv["FID"]<38766) ]
dd=df[(df['code']=='000001')|(df['code']=='399001')|(df['code']=='399006')|(df['code']=='000905')|(df['code']=='000300')]
print(dd[['name','change','open','high','low','amount']])
# print(dd[dd.columns[1:7]][0:])
# for row in df.iterrows():
#     print(row)


# import tushare as ts
#
# df=ts.get_hs300s()
# df.to_csv("e.cvs")
# print(df)

