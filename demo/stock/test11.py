import csv
import time
import datetime

# 读取csv至字典
# csvFile = open("c:/day/sh1.csv", "r")
csvFile = open("c:/day/sz.csv", "r")
reader = csv.reader(csvFile)

# 建立空字典
result = {}

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
number=0
for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    data = item[0]
    change = item[7]
    change=float(change)
    newdata = data.split('-')
    # print(data)
    # print(int(newdata[0]))
    # print(newdata[1])
    # print(newdata[2])
    # #某个日期星期几
    anyday = datetime.datetime(int(newdata[0]), int(newdata[1]), int(newdata[2])).strftime("%w")
    print(anyday)

    anyday=int(anyday)
    if anyday == 1:
        print(change)
        a1 = a1 + change
    elif anyday == 2:
        a2 = a2 + change
    elif anyday == 3:
        a3 = a3 + change
    elif anyday == 4:
        a4 = a4 + change
    elif anyday == 5:
        number=number+1
        a5 = a5 + change


print(str((a1/number) ))
print(str((a2/number) ))
print(str((a3/number) ))
print(str((a4/number) ))
print(str((a5/number) ))

# result[item[0]] = item[1]

csvFile.close()
print(result)
