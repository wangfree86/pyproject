# -*- coding: utf-8 -*-
"""
作者：邢不行

本系列帖子“量化小讲堂”，通过实际案例教初学者使用python、pandas进行金融数据处理，希望能对大家有帮助。

必读文章《10年400倍策略分享-附视频逐行讲解代码》：http://bbs.pinggu.org/thread-5558776-1-1.html

所有系列文章汇总请见：http://bbs.pinggu.org/thread-3950124-1-1.html

想要快速、系统的学习量化知识，可以参与我与论坛合作开设的《python量化投资入门》视频课程：http://www.peixun.net/view/1028.html，我会亲自授课，随问随答。
参与课程还可以免费加入我的小密圈，我每天会在圈中分享量化的所见所思，圈子介绍：http://t.xiaomiquan.com/BEiqzVB

微信：xbx_laoshi，量化交流Q群(快满)：438143420，有问题欢迎交流。

文中用到的A股数据可在www.yucezhe.com下载，这里可以下载到所有股票、从上市日起的交易数据、财务数据、分钟数据、分笔数据、逐笔数据等。
"""
import os

from demo.pandas学习 import pandastest as pd

# ========== 遍历数据文件夹中所有股票文件的文件名，得到股票代码列表stock_code_list
stock_code_list = []
for root, dirs, files in os.walk('D:/pytestdata/stock data/'):# 注意：这里请填写数据文件在您电脑中的路径
    if files:
        for f in files:
            if '.csv' in f:
                stock_code_list.append(f.split('.csv')[0])


# ========== 根据上一步得到的代码列表，遍历所有股票，将这些股票合并到一张表格all_stock中
all_stock = pd.DataFrame()

# 遍历每个创业板的股票
for code in stock_code_list:
    print code

    # 从csv文件中读取该股票数据
    stock_data = pd.read_csv('D:/pytestdata/stock data//' + code + '.csv',
                             parse_dates=[1])# 注意：这里请填写数据文件在您电脑中的路径
    stock_data.sort('date', inplace=True)# 对数据按照【date】交易日期从小到大排序

    # 计算KDJ指标
    low_list = pd.rolling_min(stock_data['low'], 9)
    low_list.fillna(value=pd.expanding_min(stock_data['low']), inplace=True)
    high_list = pd.rolling_max(stock_data['high'], 9)
    high_list.fillna(value=pd.expanding_max(stock_data['high']), inplace=True)
    rsv = (stock_data['close'] - low_list) / (high_list - low_list) * 100
    stock_data['KDJ_K'] = pd.ewma(rsv, com=2)
    stock_data['KDJ_D'] = pd.ewma(stock_data['KDJ_K'], com=2)
    stock_data['KDJ_J'] = 3 * stock_data['KDJ_K'] - 2 * stock_data['KDJ_D']
    # 计算KDJ指标金叉、死叉情况
    stock_data['KDJ_金叉死叉'] = ''
    kdj_position = stock_data['KDJ_K'] > stock_data['KDJ_D']
    stock_data.loc[kdj_position[(kdj_position == True) & (kdj_position.shift() == False)].index, 'KDJ_金叉死叉'] = '金叉'
    stock_data.loc[kdj_position[(kdj_position == False) & (kdj_position.shift() == True)].index, 'KDJ_金叉死叉'] = '死叉'

    # 通过复权价格计算接下来几个交易日的收益率
    for n in [1, 2, 3, 5, 10, 20]:
        stock_data['接下来'+str(n)+'个交易日涨跌幅'] = stock_data['adjust_price'].shift(-1*n) / stock_data['adjust_price'] - 1.0
    stock_data.dropna(how='any', inplace=True)# 删除所有有空值的数据行

    # 筛选出KDJ金叉的数据，并将这些数据合并到all_stock中
    stock_data = stock_data[(stock_data['KDJ_金叉死叉'] == '金叉')]
    if stock_data.empty:
        continue
    all_stock = all_stock.append(stock_data, ignore_index=True)

# ========== 根据上一步得到的所有股票KDJ金叉数据all_stock，统计这些股票在未来交易日中的收益情况
print
print '历史上所有股票出现KDJ金叉的次数为%d，这些股票在：' %all_stock.shape[0]
print

for n in [1, 2, 3, 5, 10, 20]:
    print "金叉之后的%d个交易日内，" % n,
    print "平均涨幅为%.2f%%，" % (all_stock['接下来'+str(n)+'个交易日涨跌幅'].mean() * 100),
    print "其中上涨股票的比例是%.2f%%。" % \
          (all_stock[all_stock['接下来'+str(n)+'个交易日涨跌幅'] > 0].shape[0]/float(all_stock.shape[0]) * 100)
    print
