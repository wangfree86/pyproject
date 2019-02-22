def save_infor(one_page_film):
    '''
    存储提取好的电影信息
    :param one_page_film: 电影信息列表
    :return: None
    '''
    with open('top_film.csv', 'a', newline='', errors='ignore') as f:
        csv_file = csv.writer(f)
    for one in one_page_film:
        csv_file.writerow([one['name'], one['start'], one['releasetime'], one['score']])


import csv


# 创建一个cvs，初二
def create_csv(path, data_row):
    with open(path, 'w+', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)


import os


def write_csv(path, data_row):
    with open(path, 'a+', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)


# 读取表格，获取最后一行的日期
def read_end_time(path):
    with open(path) as csvfile:
        mLines = csvfile.readlines()
    targetLine = mLines[-1]
    if len(targetLine) < 2:
        targetLine = mLines[-2]
        if len(targetLine) < 2:
            targetLine = mLines[-3]
    a = targetLine.split(',')[0]
    return a


def read(path):
    # 读取csv至字典
    csvFile = open(path, "r")
    reader = csv.reader(csvFile)
    return reader


import datetime


# 判断传入的时间年月日是否相等
def isequal(oldtime, uptime):
    if oldtime == uptime:
        return True
    else:
        return False


# 读csv文件返回json
def read_csv_json(path):
    csv_rows = []
    with open(path) as csvfile:
        # 获取全部数据
        reader = csv.DictReader(csvfile)
        # 获取title数据
        titles = reader.fieldnames
        for row in reader:
            dict1 = {}
            for title in titles:  # 第二个实例
                dict1.setdefault(title, row[title])
            csv_rows.append(dict1)
        # print(csv_rows)
        return csv_rows