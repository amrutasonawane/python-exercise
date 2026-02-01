#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 else false
def checkIsDivisible(no1):
	if(no1 % 5 == 0):
		return True
	else:
		return False

def main():
	value = int(input("Enter number : "))
	if(checkIsDivisible(value)):
		print("Given number is divisible by 5")
	else:
		print("Given number is not divisible by 5")


if __name__ == "__main__":
	main()