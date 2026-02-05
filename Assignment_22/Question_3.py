class Arithmetic :
	def __init__(self):
		self.Value1 = 0
		self.Value2 = 0

	def Accept(self, no1,no2):
		self.Value1 = no1
		self.Value2 = no2

	def Addition(self):
		return self.Value1 + self.Value2

	def Subtraction(self):
		return self.Value1 - self.Value2

	def Multiplication(self):
		return self.Value1 * self.Value2

	def Division(self):
		return self.Value1 / self.Value2

obj1 = Arithmetic()
obj1.Accept(10,30)
resultAdd = obj1.Addition()
resultSub = obj1.Subtraction()
resultMult = obj1.Multiplication()
resultDiv = obj1.Division()

print("result of Addition is : ",resultAdd)
print("result of Subtraction is : ",resultSub)
print("result of Multiplication is : ",resultMult)
print("result of Division is : ",resultDiv)


obj2 = Arithmetic()
obj2.Accept(50,15)
resultAdd = obj2.Addition()
resultSub = obj2.Subtraction()
resultMult = obj2.Multiplication()
resultDiv = obj2.Division()

print("result of Addition is : ",resultAdd)
print("result of Subtraction is : ",resultSub)
print("result of Multiplication is : ",resultMult)
print("result of Division is : ",resultDiv)
