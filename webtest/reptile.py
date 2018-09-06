#!/usr/bin/python
# -*-coding:utf-8 -*-
from openweb import openweb, Tool


def getPage(baseURL):
    bdtb = openweb(baseURL)

    def has_class_but_no_id(tag):
        return tag.has_attr('class')

    from bs4 import BeautifulSoup

    html = bdtb.getPage()
    soup = BeautifulSoup(html, "lxml")
    for tag in soup.find_all(class_="tag-marketcap"):
        # for tag in soup.find_all('div',class_="value"):
        for tag1 in tag.find_parents(class_="value"):
            s = tag1.contents[0]
            # print s
            s = s.replace(",", "")[1:];
            # print s
    return s


def getnowString(num):
    return str(round(float(num) / float(100000000), 5)) + '亿'


def main1():
    baseURL = 'http://www.feixiaohao.com/currencies/'
    money = ['bitshares', 'bitcny', 'bitusd']
    bitsharesi = 0;
    allnumber = 0;
    for index in range(len(money)):
        nbaseURL = baseURL + money[index] + '/'
        if money[index].find('bitshares') == -1:
            sa = getPage(nbaseURL)
            print sa
            allnumber +=float(sa );
        else:
            bitsharesi = getPage(nbaseURL);
            print bitsharesi
    print '------------'
    print allnumber
    print bitsharesi
    print str(round(float(allnumber) / float(bitsharesi), 5) * 100) + "%"


main1()
# main1()
# 333004583
# 10009597326
