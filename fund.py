import tushare as ts

dd = ts.fund_holdings(2017, 3)

import pandas as pd

writer = pd.ExcelWriter('D:\pyproject\excel\\fund.xlsx', engine='xlsxwriter')

dd.to_excel(writer)
writer.save()
