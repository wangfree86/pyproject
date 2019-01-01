# -*- coding: utf-8 -*-
"""
@author: Xingbuxing
date: 2017年05月06日
本程序示例如何将日线数据转换为周线数据、以及resample函数的使用方式
"""
import pandas as pd
from program import Functions
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# =====读入数据
code = 'sz300001'
df = Functions.import_stock_data(code)


# =====以日线数据转化为周线数据为例，
# ===上课资料文件夹中的《日线转周线说明》
# ===将'交易日期'这一列设置为index，之后讲为什么需要这么做
df.set_index('交易日期', inplace=True)

# ===周期转换方法：resample
week_df = df.resample(rule='w').last()
# 'w'意思是week，意味着转变为周线；
# last意思是取最后一个值
# 查看week_df中2009-11-08这一行的数据
# print df.iloc[:7]
# print week_df
# exit()

# 这一周的开、高、低的价格
week_df['开盘价'] = df['开盘价'].resample('w').first()
week_df['最高价'] = df['最高价'].resample('w').max()
week_df['最低价'] = df['最低价'].resample('w').min()
week_df['成交量'] = df['成交量'].resample('w').sum()

# 计算这一周的涨跌幅
# 不能使用：（最后一天的收盘价 - 第一天的收盘价） / 第一天的收盘价
# 使用每天的涨跌幅连乘，没有现成的函数，使用apply方式
week_df['涨跌幅'] = df['涨跌幅'].resample('w').apply(lambda x: (x + 1.0).prod() - 1.0)

# 计算这一周的交易天数
week_df['交易天数'] = df['收盘价'].resample('w').size()
# print df.iloc[:7]
# print week_df


# ===去除一天都没有交易的周
# 发现2010-02-21这一行，所有的值都是空的。
# resample会将每一周都列出来，不管这一周是否有交易
week_df.dropna(subset=['成交量'], how='any', inplace=True)

# ===保留这一周最后一个交易期
# week_df的index并不是这一周最后一个交易日，而是这一周星期天的日期。
# 如何才能保留这周最后一个交易日的日期？
# 在将'交易日期'set_index之前，先增加df['最后交易日'] = df['交易日期']，然后在resample的时候取'最后交易日'的last就是最后一个交易日
# 这个操作可以自己尝试完成

# ===为什么在一开始时候需要set_index？
# 因为进行resample操作的前提：以时间变量作为index
# 在0.19版本的pandas开始，resample函数新增on参数，可以不事先将时间变量设置为index。
# 具体可见：http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.resample.html
# 如何查看自己的pandas版本？
# print pd.__version__  # 所有package都可以通过这个方式来查看版本。或者在PyCharm中查看

# ===rule的取值
# rule='w'代表转化为周
# 'm'代表月，'q'代表季度，'y'代表年份。'5min'代表5分钟，'1min'，等等

# 非常人性化的ohlc函数
# print df['收盘价'].resample(rule='w').ohlc()  # 直接将收盘价这个序列，转变为周线，并且计算出open、high、low、close
