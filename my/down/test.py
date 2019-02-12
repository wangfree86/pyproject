#使用os.unlink()和os.remove()来删除文件
#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-
import os
my_file = 'D:/text.txt'
if os.path.exists(my_file):
    #删除文件，可使用以下两种方法。
    os.remove(my_file)
    #os.unlink(my_file)
else:
    print ('no such file:%s'%my_file)