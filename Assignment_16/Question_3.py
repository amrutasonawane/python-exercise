#Write a program which contains one function -> which accepts two numbers from user and return addition 

def addition(no1,no2):
	return no1 + no2

def main():
	value1 = int(input("Enter first number : "))
	value2 = int(input("Enter second number : "))
	result = addition(value1,value2)
	print("Addition of given number is : ",result)

if __name__ == "__main__":
	main()

