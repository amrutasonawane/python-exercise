#Write a program which accept one number from user and return its factorial

def factorial(num1):
	result = 1
	for i in range(1,num1+1):
		result= i * result
	return result

def main():
	number = int(input("Enter number : "))
	result = factorial(number)
	print("Factorial of given number is : ", result)

if __name__ == "__main__":
	main()