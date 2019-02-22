# -*- coding: utf-8 -*-
"""
@author: Xingbuxing
date: 2017年05月06日
apply操作说明

"""
import pandas as pd
import Functions
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行


# 读入数据
code = 'sz300001'
df = Functions.import_stock_data(code)

# 当想要进行的操作，在pandas当中，没有相应直接可用的函数的时候，可以使用apply方法
# apply的参数是函数名
# 以下定义几个简单的函数，演示apply


def f12(x,y):
    # print x
    print (type(x))
    print (y[0:3])
    exit()
    return x + 10000
    # x究竟是什么？

    # x就是['收盘价']这个series，对series可以进行的任何操作，在f1中都可以进行。可以进行很复杂的操作。
# print apply(f12,(df[['收盘价']],df[['收盘价']]))[0:11]


# lambda函数定义方法
# 通常用于定义一些比较简单的、一行代码可以表述清楚的、一次性的函数。比较复杂就不要使用。
# 以下是几个案例

# print df['收盘价'].apply(lambda x: int(x * 100))
# print df['股票代码'].apply(lambda x: x[2:3] + x[:2].upper())[0:9]
exit()

# apply、lambda是较高级的应用，大家一开始不用强行使用。之后看的多了自然也就理解会用了