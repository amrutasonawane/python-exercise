import arithmetic

def main():
	value1 = int(input("Enter first number : "))
	value2 = int(input("Enter second number : "))
	result = arithmetic.addition(value1,value2)
	print("Addition of 2 numbers is : ",result)
	result =  arithmetic.subtraction(value1,value2)
	print("Subtraction of 2 number is : ",result)
	result =  arithmetic.division(value1,value2)
	print("Division of 2 number is : ",result)
	result =  arithmetic.multiplication(value1,value2)
	print("Multiplication of 2 number is : ",result)


if __name__ == "__main__":
	main()