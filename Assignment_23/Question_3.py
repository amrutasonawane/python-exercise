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
		for i in range (1,(self.Value // 2) + 1):
			if(self.Value % i ) == 0:
				number = number + i
		if(number == self.Value):
			return True
		else:
			return False

	def getFactors(self):
		allFactors = []
		for i in range (1,(self.Value // 2) + 1):
			if(self.Value % i) == 0 :
				allFactors.append(i)
		return allFactors

	def sumFactors(self):
		sum = 0
		allFactors = self.getFactors()
		for i in range(len(allFactors)):
			sum = sum + allFactors[i]
		return sum

obj1 = Numbers(15)
if(obj1.checkPrime()):
	print("Given number is prime")
else:
	print("Given number is not prime")

if(obj1.checkPerfect()):
	print("Given number is perfect number")
else:
	print("Given number is not perfect number")

Result = obj1.getFactors()
print("Factors of given number is : ",Result)

sumOfFactors = obj1.sumFactors()
print("Sum of all factors of given number is : ",sumOfFactors)	
