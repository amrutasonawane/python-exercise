#Write a program which accept number from user and return addition of digits in that num

def sumDigit(num1):
	num_str = str(num1)
	result = 0
	for i in (num_str):
		result = result + int(i)
	return result		

def main():
	value = input("Enter number : ")
	print("Sum of number of entered digit is : ",sumDigit(value))

if __name__  == "__main__":
	main()