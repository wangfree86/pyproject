# 
# import requests, json
# f=open(r'test.txt','r')#打开所保存的cookies内容文件
# cookies={}#初始化cookies字典变量
# for line in f.read().split(';'):   #按照字符：进行划分读取
#     #其设置为1就会把字符串拆分成2份
#     name,value=line.strip().split('=',1)
#     cookies[name]=value  #为字典cookies添加内容
# 
# 
# base_url = "http://service.5sing.kugou.com/song/getPermission?jsoncallback=jQuery17036960075558330574_1536831322587&songId=3676331&songType=1&_=1536831322587"
# res=requests.get(base_url,cookies=cookies)
# # soup = BeautifulSoup(res, features='lxml')
# print(res)
# html = json.loads(res.text)
# print(html)
# print(html)
# # next_page = html['next_page']
# # print('下一页地址:',next_page)
# # for each in html['photos']:
# #     print('图片ID:',each['id']
# 
