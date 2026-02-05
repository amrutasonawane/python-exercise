class Demo:
	Value = 0
	def __init__(self,value1, value2):
		self.no1 = value1
		self.no2 = value2

	def fun(self):
		print(obj1.no1)
		print(obj1.no2)

	def gun(self):
		print(obj2.no1)
		print(obj2.no2)

obj1 = Demo(10,11)
obj2 = Demo(100,110)

obj1.fun()
obj1.gun()

obj2.fun()
obj2.gun()