# 例如，要导入模块 fibo 的 fib 函数，使用如下语句：
#
# >>> from fibo import fib, fib2
# from … import * 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
#
# from modname import *
# http://www.runoob.com/python3/python3-module.html
# 关于类之间引用的方法
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
from A import A
a=A(2,3)
a.add()
