#1. Write a program which accepts one number and checks whether it is prime or not.
#Input: 11
#Output: Prime Number
def checkPrime(no1):
	if(no1 == 0 or no1 == 1):
		return False
	for i in range(2,int(no1/2)):
		if (no1 % i == 0):
			return False
	else :
		return True

def main():
	value = int(input("Enter a number : "))
	flag = checkPrime(value)
	if(flag):
		print("Given number is Prime")
	else:
		print("Given number is not Prime")

if __name__ == "__main__":
 	main()