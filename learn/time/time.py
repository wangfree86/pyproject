import datetime
import time

t = time.time()

print (t)                       #原始时间数据
print (int(t))                  #秒级时间戳
print (int(round(t * 1000)))    #毫秒级时间戳

nowTime = lambda:int(round(t * 1000))
print (nowTime());              #毫秒级时间戳，基于lambda

print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化
print (datetime.datetime.now().strftime('%Y-%m-%d'))   #日期格式化
# ---------------------------------------------------------------------------------------------------------------
print (int(round(time.time() * 1000)))#毫秒级时间戳