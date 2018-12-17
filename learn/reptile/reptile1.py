from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import requests
class downloader(object):
    def __init__(self):
        self.server = 'https://tieba.baidu.com/p/2256306796?pn='
        self.all = 1
        self.allsrc = 0
        self.name = []          #存放


    """
        获取全部链接
          """
    def get_download_url(self,number):
        url=self.server+number
        print(url)
        # 获取网页内容
        html = requests.get(url).text
        # 获取网页元素
        soup = BeautifulSoup(html, 'lxml')
        # 根据条件筛选元素
        img_ul = soup.find_all('img', class_ ="BDE_Image")
        for i,each in enumerate(img_ul):
            src=each.get('src')
            self.allsrc = self.allsrc + 1
            print(src)
        newstr="当前页码："+number +"    下载链接数量："+ str(self.allsrc)
        print(newstr)
        self.name.append(newstr)
            # import requests
            # r = requests.get(src)
            # with open('../img/'+str(i)+'.png', 'wb') as f:
            #     f.write(r.content)
# req = requests.get(url=self.target+str)
        # html = req.text
        # div_bf = BeautifulSoup(html)
        # div = div_bf.find_all('div', class_='listmain')
        # a_bf = BeautifulSoup(str(div[0]))
        # a = a_bf.find_all('a')
        # self.nums = len(a[15:])  # 剔除不必要的章节，并统计章节数
        # for each in a[15:]:
        #     self.names.append(each.string)
        #     self.urls.append(self.server + each.get('href'))


if __name__ == "__main__":
        dl = downloader()
        for n in range(1, dl.all+1):
            n=str(n)
            dl.get_download_url(n)
            print("当前页码"+n)

        print("总src量"+str(dl.name))
#         print(newstr)
# self.name.append(newstr)
        # for i in range(dl.nums):
        #     dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
        #     sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        #     sys.stdout.flush()
        # print('《一年永恒》下载完成')

#
# base_url = "https://tieba.baidu.com/p/2256306796?pn="
#
# url = base_url
# l_pager
# pager_theme_4
# pb_list_pager
# html = urlopen(url).read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')
#
# div = soup.find_all('img', class_='BDE_Image')
#
# for i, each in enumerate(div):
#     # if i<3:
#     print(i)
#     src = each.get('src')
#     import requests
#
#     r = requests.get(src)
#     with open('../img/' + str(i) + '.png', 'wb') as f:
#         f.write(r.content)
#
#         # print [i for i, x in enumerate(your_list) if x == 'your_item']
#         # your_list为待查list，your_item为具体要查的元素
#         # 打印出一个包含所有要查元素下标的列表
#
#         # print(BeautifulSoup(str(div[0])).find_all('img'))
#         # print(div[0].find_all('src'))
#         # print(div[1].src)
#         # print(soup.find('h1').get_text(), '    url: ', his[-1])
