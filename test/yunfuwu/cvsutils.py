

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
    with open(path, 'w+') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)


import os


def write_csv(path, data_row):
    if os.path.exists(path):
        with open(path, 'a+') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(data_row)
    else:
        create_csv()


# 读取表格，获取最后一行的日期
def read_csv(path):
    with open(path) as csvfile:
        mLines = csvfile.readlines()
    targetLine = mLines[-1]
    if len(targetLine) < 2:
        targetLine = mLines[-2]
    a = targetLine.split(',')[0]
    return a


import datetime


# 判断传入的时间年月日是否相等
def isequal(oldtime, uptime):
    # ntime = datetime.datetime.now().strftime('%Y-%m-%d')
    if oldtime == oldtime:
        return True
    else:
        return False


if __name__ == "__main__":
    # create_csv()
    # for a in range(10):
    #     write_csv()
    #     print(a)
    isequal('2019-02-13 09:19:18')
    # dl = GetStock()
    # dd=dl.getAllStock()
    # print("--"+dd)
