#Write a program which accept one number from user and return addition of its factors
def addFact(num1):
	result = 0
	for i in range(1,(num1 // 2)+1):
		if (num1 %i == 0) :
			result = result + i
	return result

def main():
	number = int(input("Enter number : "))
	result = addFact(number)
	print("Factorial of given number is : ", result)

if __name__ == "__main__":
	main()