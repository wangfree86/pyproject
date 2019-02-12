# -*- coding: utf-8 -*-
"""
@author: Xingbuxing
date: 2017年05月06日
本程序示例如何批量导入数据，并且使用hdf方式存储
"""
import os
import pandas as pd
from program import Functions
from program import config
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# 导入单个股票的数据
code = 'sz300001'
df = Functions.import_stock_data(code)

# =====批量导入股票数据
# 系统自带函数os.walk，用于遍历文件夹中的所有文件，os是python自带的系统库
# 演示os.walk
# for root, dirs, files in os.walk(config.input_data_path):
#     # root输出文件夹，dirs输出root下所有的文件夹，files输出root下的所有的文件
#     print 'root:', root
#     print 'dirs:', dirs
#     print 'files:', files
#     print

# ===批量读取文件名称
stock_list = []
data_path = config.input_data_path + '/stock_data'
for root, dirs, files in os.walk(data_path):
    # 当files不为空的时候
    if files:
        for f in files:
            if f.endswith('.csv'):
                stock_list.append(f[:8])

# ===批量导入股票数据
all_stock_data = pd.DataFrame()
for code in stock_list:
    print code
    # 导入数据
    df = Functions.import_stock_data(code)
    # 合并数据
    all_stock_data = all_stock_data.append(df, ignore_index=True)  # 注意此时若一下子导入很多股票的时候，可能会内存溢出
print all_stock_data

# 将数据存入hdf文件中
all_stock_data.to_hdf(
    config.output_data_path + '/all_stock_data_h5.h5',
    key='all_stock_data',
    mode='w')

# print pd.read_hdf(config.output_data_path + '/all_stock_data_h5.h5', key='all_stock_data')
# exit()

# =====将数据存入hdf文件
# # 创建hdf文件
# h5_store = pd.HDFStore(config.output_data_path + '/stock_data_H5_1.h5', mode='w')
# # 批量读取股票并且存如store
# for code in stock_list:
#     print code
#     # 导入数据
#     df = Functions.import_stock_data(code)
#     # 存储数据方式1
#     h5_store[code] = df
#     # 存储数据方式2
#     df.to_hdf(config.output_data_path + '/stock_data_H5_2.h5', key=code, mode='a')
# # 关闭hdf文件
# h5_store.close()

# =====读取hdf数据
# 创建hdf文件
# h5_store = pd.HDFStore(config.otput_data_path + '/stock_data_H5_1.h5', mode='r')
# h5_store中的key
# print h5_store.keys()
# 读取某个key指向的数据
# print h5_store.get('sz000006')
# print h5_store['sz000007']
# 关闭hdf文件
# h5_store.close()


# 另外一种方式读取hdf数据
# print pd.read_hdf(
#     config.output_data_path + '/stock_data_H5_2.h5',
#     key='sz000006'
# )
