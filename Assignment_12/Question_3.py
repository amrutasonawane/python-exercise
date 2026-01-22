#Write a program which accept 2 numbers and prints addition, subtraction, multiplication and division
def addition(no1,no2):
	return no1+no2

def subtraction(no1,no2):
	return no1-no2
def multiplication(no1,no2):
 return no1*no2
def division(no1,no2):
	return no1/no2

def main():
	result = 0
	value1 = int(input("Enter first number : "))
	value2  = int(input("Enter second number : "))
	result = addition(value1 ,value2)
	print("Result of addition of is : ", result)
	result = subtraction(value1 , value2)
	print("Result of subtraction of is : ", result)
	result = multiplication(value1, value2)
	print("Result of multiplication of is : ", result)
	result = division(value1, value2)
	print("Result of division of is : ", result)




if __name__ == "__main__":
	main()