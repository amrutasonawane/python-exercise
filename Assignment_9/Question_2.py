#2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
def checkGreater(no1,no2):
	if(no1>no2):
		return no1
	else:
		return no2





def main():
	value1 = input("Enter first number : ")
	value2 = input("Enter second number : ")
	result  = checkGreater(value1,value2)
	print("Greater number is :",result)

if __name__ == "__main__":
	main()