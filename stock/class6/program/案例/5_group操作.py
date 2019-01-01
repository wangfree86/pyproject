# -*- coding: utf-8 -*-
"""
@author: Xingbuxing
date: 2017年05月06日
本程序展示group_by操作
"""
import pandas as pd
from program import config
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# 从hdf文件中导入数据
stock_data = pd.read_hdf(config.output_data_path + '/all_stock_data_h5.h5', key='all_stock_data')

# =====groupby常用操作汇总
# 根据'交易日期'进行group，将相同'交易日期'的行放入一个group，
# print stock_data.groupby('交易日期')  # 生成一个group对象。不会做实质性操作，只是会判断是否可以根据该变量进行groupby

# group后可以使用相关函数，size()计算每个group的行数
# print stock_data.groupby('交易日期').size()  # 每天交易股票的个数
# 根据'股票代码'进行group，将相同'交易日期'的行放入一个group，
# print stock_data.groupby('股票代码').size()  # 每只股票交易的天数

# 获取其中某一个group
# print stock_data.groupby('股票代码').get_group('sz000007')


# 其他常见函数
# print stock_data.groupby('股票代码').describe()  # 只会对数值变量进行describe
# print stock_data.groupby('股票代码').head(3)
# print stock_data.groupby('股票代码').tail(3)  # 每个group里面的行顺序，会保留。
# print stock_data.groupby('股票代码').first()
# print stock_data.groupby('股票代码').last()
# print stock_data.groupby('股票代码').nth(2)
# 将group变量不设置为index
# print stock_data.groupby('股票代码', as_index=False).nth(2)

# 在group之后，取一部分变量进行计算
# 计算每个group的均值
# print stock_data.groupby('股票代码')['收盘价', '涨跌幅'].mean()
# 计算每个group的最大值
# print stock_data.groupby('股票代码')['收盘价', '涨跌幅'].max()
# 计算每个group的加总
# print stock_data.groupby('股票代码')['成交量'].sum()
# 计算该数据在每个group中的排名
# print stock_data.groupby('股票代码')['成交量'].rank()
# print stock_data.groupby('股票代码')['成交量'].rank(pct=True)

# 如何根据年份进行group
# print stock_data.groupby('交易日期').size()
# print stock_data.groupby(stock_data['交易日期'].dt.year).size()

# 也可以同时用多个变量来进行group，将这些变量的值都相同的行
# print stock_data.groupby(['股票代码', stock_data['交易日期'].dt.year]).size()

# 我们之前讲过的resample、fillna、apply等常见操作，在group里面都可以进行。
# 这些操作需要大家有一定的积累，若直接在group上进行这些操作不熟练，可以使用已下的方式。

# 遍历group，对每个group进行单独操作，然后将这些group合并起来。
# 语法：for key, group in df.groupby('列名'):

for code, group in stock_data.groupby('股票代码'):
    print code
    print group

    # 以下可以对各个group进行任意操作。
    group.fillna()
    group.apply()

    # 操作完之后，将这些group再append起来

# 在一开始不熟练的时候，可以多用遍历每个group的方式
