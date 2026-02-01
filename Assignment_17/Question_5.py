#Write a program which accept one number for user and check whether number is prime or not
def checkPrime(value):
	for i in range(2,(value//2)+1):
		if value % i == 0:
			return False
	return True


def main():
	value = int(input("Enter number : "))
	if(checkPrime(value)):
		print("Enter number is Prime")
	else:
		print("Enter number is not prime")


if __name__ == "__main__":
	main()