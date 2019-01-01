import requests
import re
import csv
import time

# 操作csv的一天简单demo
if __name__ == "__main__":
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        ]

with open('stocks.csv', 'w') as f:
    f_csv = csv.writer(f)
    # 添加header
    f_csv.writerow(headers)
    # 添加列表
    f_csv.writerows(rows)
