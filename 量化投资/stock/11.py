# -*- coding: utf-8 -*-
"""
@author: yucezhe
@contact: QQ:2089973054 email:xjc@yucezhe.com
【量化小讲堂 - python & pandas技巧系列】使用python计算移动平均线
"""
from demo import pandastest as pd

# ========== 从原始csv文件中导入股票数据，以浦发银行sh600000为例

# 导入数据 - 注意：这里请填写数据文件在您电脑中的路径
stock_data = pd.read_csv('sh600519.csv', parse_dates=[1])

# 将数据按照交易日期从远到近排序
# stock_data.sort_values('date', inplace=True)


# ========== 计算移动平均线

# 分别计算5日、20日、60日的移动平均线
ma_list = [2, 20, 160]

# 计算简单算术移动平均线MA - 注意：stock_data['close']为股票每天的收盘价
for ma in ma_list:
    stock_data['MA_' + str(ma)] = pd.rolling_mean(stock_data['close'], ma)

# 计算指数平滑移动平均线EMA
# for ma in ma_list:
#     stock_data['EMA_' + str(ma)] = pd.ewma(stock_data['close'], span=ma)

# 将数据按照交易日期从近到远排序
stock_data.sort('date', ascending=False, inplace=True)

# ========== 将算好的数据输出到csv文件 - 注意：这里请填写输出文件在您电脑中的路径
stock_data.to_csv('sh600000_ma_ema.csv', index=False)