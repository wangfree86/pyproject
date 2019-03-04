# -*- coding: utf-8 -*-
"""
@author: Xingbuxing
date: 2017年05月14日
本段程序用于演示策略评价指标
"""
import pandas as pd  # 导入pandas，我们一般为pandas去一个别名叫做pd
import config

print("11111111")
# ===导入数据
select_stock = pd.read_hdf(config.output_data_path + '/市值选股结果.h5', 'select_stock')
print("2222222")
# equity = pd.read_hdf(program.config.output_data_path + '/市值选股结果.h5', 'equity')
