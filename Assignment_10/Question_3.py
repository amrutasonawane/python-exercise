#Write a program which accepts one number and prints factorial of that number.


def factorialNum(no1):
	result = 1
	for i in range(1,no1+1):
		result = result * i
	return result


def main():
	fact =  factorialNum(5)
	print("factorial of given number is : ", fact)

if __name__ == "__main__":
	main()