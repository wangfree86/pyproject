# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# =====读入数据
df = pd.DataFrame()
for file_name in ['sh600000上.csv', 'sh600000下.csv']:
    # 导入数据
    temp = pd.read_csv(file_name, encoding='gbk')
    # 合并数据
    df = df.append(temp, ignore_index=True)


# =====整理数据
df.columns = [i.encode('utf8') for i in df.columns]
df = df[['交易日期', '股票代码', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅']]
df['交易日期'] = pd.to_datetime(df['交易日期'])


# =====去除重复值
df.drop_duplicates(inplace=True)
df.sort_values(by=['交易日期'], inplace=True)
df.reset_index(inplace=True, drop=True)


# =====完成作业一
# 2017年4月24日涨幅：
print '上市第一天涨跌幅：', df.iloc[0]['涨跌幅']

# 最近一个交易日收盘价：
print '最近一个交易日收盘价：', df.iloc[-1]['收盘价']

# 所有星期二的平均涨幅:
print '所有星期二的平均涨幅：', df[df['交易日期'].dt.weekday == 1]['涨跌幅'].mean()

# 涨幅大于5%的天数
print '涨幅大于5%的天数：', df[df['涨跌幅'] >= 0.05]['涨跌幅'].count()

# 2016年涨幅：
print '2016年涨幅：', (df[(df['交易日期'].dt.year == 2016)]['涨跌幅'] + 1).prod() - 1


# =====完成作业二
df['最近20个交易日最高价'] = df['最高价'].rolling(20).max()
df['最近20个交易日最低价'] = df['最低价'].rolling(20).min()

idx = df[df['收盘价'] > df['最近20个交易日最高价'].shift()].index
df.loc[idx, '信号'] = '买入点'

idx = df[df['收盘价'] < df['最近20个交易日最低价'].shift()].index
df.loc[idx, '信号'] = '卖出点'

df.to_csv('sh600000海龟交易法则买卖点.csv', index=False, encoding='gbk')
