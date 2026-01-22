#Write a program which accepts one number and prints all even numbers till that number.


def checkEven(no1):
	result =[]
	for i in range (1,no1+1):
		if(i % 2==0):
			result.append(i)
	return result

def main():
	value = int(input("Enter number : "))
	result  = checkEven(value)
	print("Factorial of given number is : ",result)

if __name__ == "__main__":
	main()