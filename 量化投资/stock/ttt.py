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
from demo.pandas学习 import pandastest as pd

# ==========导入上证指数的原始数据
# 注意：这里请填写数据文件在您电脑中的路径，并注意路径中斜杠的方向
index_data = pd.read_csv('sh600519.csv', parse_dates=['date'])
# 保留这几个需要的字段：'date', 'high', 'low', 'close', 'change'
index_data = index_data[['date', 'high', 'low', 'close', 'change']]
# 对数据按照【date】交易日期从小到大排序
index_data.sort('date', inplace=True)


# ==========计算海龟交易法则的买卖点
# 设定海龟交易法则的两个参数，当收盘价大于最近N1天的最高价时买入，当收盘价低于最近N2天的最低价时卖出
# 这两个参数可以自行调整大小，但是一般N1 > N2
N1 = 20
N2 = 10

# 通过rolling_max方法计算最近N1个交易日的最高价
index_data['最近N1个交易日的最高点'] =  pd.rolling_max(index_data['high'], N1)
# 对于上市不足N1天的数据，取上市至今的最高价
index_data['最近N1个交易日的最高点'].fillna(value=pd.expanding_max(index_data['high']), inplace=True)

# 通过相似的方法计算最近N2个交易日的最低价
index_data['最近N2个交易日的最低点'] =  pd.rolling_min(index_data['low'], N1)
index_data['最近N2个交易日的最低点'].fillna(value=pd.expanding_min(index_data['low']), inplace=True)

# 当当天的【close】> 昨天的【最近N1个交易日的最高点】时，将【收盘发出的信号】设定为1
buy_index = index_data[index_data['close'] > index_data['最近N1个交易日的最高点'].shift(1)].index
index_data.loc[buy_index, '收盘发出的信号'] = 1
# 当当天的【close】< 昨天的【最近N2个交易日的最低点】时，将【收盘发出的信号】设定为0
sell_index = index_data[index_data['close'] < index_data['最近N2个交易日的最低点'].shift(1)].index
index_data.loc[sell_index, '收盘发出的信号'] = 0

# 计算每天的仓位，当天持有上证指数时，仓位为1，当天不持有上证指数时，仓位为0
index_data['当天的仓位'] = index_data['收盘发出的信号'].shift(1)
index_data['当天的仓位'].fillna(method='ffill', inplace=True)

# 取1992年之后的数据，排出较早的数据
index_data = index_data[index_data['date'] >= pd.to_datetime('19930101')]

# 当仓位为1时，买入上证指数，当仓位为0时，空仓。计算从19920101至今的资金指数
index_data['资金指数'] = (index_data['change'] * index_data['当天的仓位'] + 1.0).cumprod()
initial_idx = index_data.iloc[0]['close'] / (1 + index_data.iloc[0]['change'])
index_data['资金指数'] *= initial_idx

# 输出数据到指定文件
index_data[['date', 'high', 'low', 'close', 'change', '最近N1个交易日的最高点',
            '最近N2个交易日的最低点', '当天的仓位', '资金指数']].to_csv('turtle.csv', index=False, encoding='gbk')


# ==========计算每年指数的收益以及海龟交易法则的收益
index_data['海龟法则每日涨跌幅'] = index_data['change'] * index_data['当天的仓位']
year_rtn = index_data.set_index('date')[['change', '海龟法则每日涨跌幅']]. \
               resample('A', how=lambda x: (x+1.0).prod() - 1.0) * 100
print year_rtn