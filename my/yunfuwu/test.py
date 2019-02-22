from GetStock import *
from GetCoin import *
# 单元测试代码
class getAll:

    if __name__ == "__main__":
        # dl = GetStock()
        # dd=dl.getAllStock()
        # print("--"+dd)
        dl = GetCoin()
        dd=dl.getAllCoin()
        print("--"+dd)

        # ntime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # # 如果不一样说明是新一天数据需要保存targetLine.split(',')[0]
        # if csv.isequal(csv.read_end_time('纳指3倍空.csv').split(' ')[0],ntime.split(' ')[0]):
        #     print('dddddd')
        # else:
        #     print('ee')

