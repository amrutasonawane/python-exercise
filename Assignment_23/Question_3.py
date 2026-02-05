class Numbers :
	def __init__(self, no1):
		self.Value = no1

	def checkPrime(self):	
		for i in range(2,(self.Value//2)+1):
			if (self.Value % 1) == 0 :
				return False
		else:
			return True

	def checkPerfect(self):
		number = 0
		for i in range (1,self.Value // 2):
			if(self.Value % i ) == 0:
				number = number + i
				print(number)
		if(number == self.Value):
			return True
		else:
			return False

obj1 = Numbers(28)
if(obj1.checkPrime()):
	print("Given number is prime")
else:
	print("Given number is not prime")

if(obj1.checkPerfect()):
	print("Given number is perfect number")
else:
	print("Given number is not perfect number")
		
