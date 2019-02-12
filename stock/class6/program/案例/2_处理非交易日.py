# -*- coding: utf-8 -*-
"""
@author: Xingbuxing
date: 2017年05月06日
本程序示例如何处理非交易日、以及merge函数的使用方式
"""
import pandas as pd
import Functions
import config
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# =====数据导入
# ===导入股票数据
# 读入数据
code = 'sz300001'
df = Functions.import_stock_data(code)
# print df
start_date = df.iloc[0]['交易日期']  # 取数据开始的日期
end_date = df.iloc[-1]['交易日期']  # 取数据结束的日期

# ===导入指数数据
# 选取日期
df_index = Functions.import_sh000001_data()

df_index.rename(columns={'大盘涨跌幅': '涨跌幅'}, inplace=True)  # 对列名重命名
df_index = df_index[(df_index['交易日期'] >= start_date) &
                    (df_index['交易日期'] <= end_date)]


# =====将指数数据和股票数据进行横向合并
# ===上课资料文件夹中的《merge函数解释》，说明横向合并的含义。
# ===使用merge函数
df = pd.merge(
    left=df,  # 两个表合并，放在左边的表
    right=df_index,  # 两个表合并，放在右边的表
    on=['交易日期'],  # 以哪个变量作为合并的主键，可以是多个，但是一定要在两张表中都存在。
    how='outer',
    # left：只保留左表的主键，right：只保留右表的主键，
    # outer：两边的主键都保留，inner：两边都有的主键才保留
    # 此处使用outer和right都可以
    sort=True,  # 结果数据是否按照主键进行排序
    suffixes=['_股票', '_指数'],  # 若两边除了主键之外有相同的列名，给这些列加上后缀
    # indicator=True  # 增加_merge列，表明这一行数据来自哪个表
)
# print df_index
# exit()
# ===查看2016年3月14日停盘附近的数据
print df[df['交易日期'] >= pd.to_datetime('20160310')]

# ===填补合并之后的缺失值
# 对于'股票代码', '收盘价'，应该如何填补？
df[['股票代码', '收盘价']] = df[['股票代码', '收盘价']].fillna(method='ffill')
# 对于开盘价、最高价、最低价，应该如何填补？
df['开盘价'] = df['开盘价'].fillna(value=df['收盘价'])
df['最高价'] = df['最高价'].fillna(value=df['收盘价'])
df['最低价'] = df['最低价'].fillna(value=df['收盘价'])
# 对于'成交量', '涨跌幅_股票'，应该如何填补？
df[['成交量', '涨跌幅_股票']] = df[['成交量', '涨跌幅_股票']].fillna(value=0)
# print df[df['交易日期'] >= pd.to_datetime('20160310')]

# ===判断当天是否交易，增加一列"是否交易"，判断这个股票今天是否交易
df.loc[df[df['成交量'] != 0].index, '是否交易'] = 1
df['是否交易'].fillna(value=0, inplace=True)
# print df[df['交易日期'] >= pd.to_datetime('20160310')]


# =====输出
df.to_csv(config.output_data_path + '/sz300000_after_merge.csv', index=False, encoding='gbk')


# merge函数非常的常用，一定要将几个参数理解、吃透（left、right、how等）
