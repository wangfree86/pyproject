# coding=utf-8
import json
import sys
from TGetStock import *
import utils.cvsutils as cvs
import constant
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    body = u'<h1>乱码Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    getcvs();
    body= cvs.read_csv_json(constant.savecsv + 'a股2倍多.csv')
    # name=environ['PATH_INFO'][1:]
    # dl = TGetStock()
    # dd=dl.getStock(name)
    # print(dd)
    # body =dd
    return [str(body).encode('utf-8')]
def p():
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    json1 = json.dumps(data)
    print (json1)
    return json1

def getcvs():
    t= cvs.read_end_time(constant.savecsv+'a股2倍多.csv')
    print(t)
    return cvs