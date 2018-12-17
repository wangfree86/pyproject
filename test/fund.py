import tushare as ts

ts.get_hist_data('600848') #一次性获取全部日k线数据

from demo import pandastest as pd

writer = pd.ExcelWriter('D:\pyproject\excel\\fund.xlsx', engine='xlsxwriter')

dd.to_excel(writer)
writer.save()
