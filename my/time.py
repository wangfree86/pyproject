import calendar
import datetime
# https://www.cnblogs.com/bovenson/p/6604803.html
# 获取当前年月后获取当前月的天数
allday=calendar.monthrange(datetime.datetime.now().year,datetime.datetime.now().month)[1]
newday=datetime.datetime.now().day
print("本月剩余天数："+str(allday-newday))

# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)