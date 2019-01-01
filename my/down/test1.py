#coding=utf-8

#定义父类  用于单位转换
class ScaleConverter:
	def __init__(self,unit_from,unit_to,factor):  #第一个参数必须是self
		self.unit_from=unit_from
		self.unit_to=unit_to
		self.factor=factor
	def description(self):    #函数必须传入self，self用于区分是哪个对象调用该方法
		return 'Convert '+self.unit_from+' to '+self.unit_to
	def convert(self,value):
		return value*self.factor


c1=ScaleConverter('inches','mm',25)  #实例化类
print(c1.description())
print(str(c1.convert(2))+c1.unit_to)


#============================================================================


class ScaleAndOffsetConverter(ScaleConverter):    # 定义子类，类继承
	def __init__(self,unit_from,unit_to,factor,offset):
		ScaleConverter.__init__(self,unit_from,unit_to,factor)   #通过父类的init()函数构造
		self.offset=offset
	def convert(self,value):     #覆盖父类的convert()函数
		return value*self.factor+self.offset


c2=ScaleAndOffsetConverter('C','F',1.8,32)  #实例化类
print(c2.description())
print(str(c2.convert(20))+c2.unit_to)