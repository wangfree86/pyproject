# coding=utf-8
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

# 百度贴吧爬虫类
class openweb:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl):
        self.baseURL = baseUrl


        # 传入页码，获取该页帖子的代码
    def getPage(self):
        try:
            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"错误原因", e.reason
                return None

 #处理页面标签类
class Tool:
     #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
     #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
     #把换行的标签换为 n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
     #将表格制表<td>替换为 t
    replaceTD= re.compile('<td>')
     #把段落开头换为 n加空两格
    replacePara = re.compile('<p.*?>')
     #将换行符或双换行符替换为 n
    replaceBR = re.compile('<br><br>|<br>')
     #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine," n",x)
        x = re.sub(self.replaceTD," t",x)
        x = re.sub(self.replacePara," n    ",x)
        x = re.sub(self.replaceBR," n",x)
        x = re.sub(self.removeExtraTag,"",x)
         #strip()将前后多余内容删除
        return x.strip()