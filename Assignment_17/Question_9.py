#Write a program which accept number from user and return number of digits in that number
def displayLength(num1):
	return int(len(num1))

def main():
	value = input("Enter number : ")
	print("Length of number of entered digit is : ",displayLength(value))

if __name__  == "__main__":
	main()