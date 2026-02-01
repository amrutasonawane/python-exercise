#Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime function which is part of our user defined module named as Marvellous Num. Name of the function from main python file should be ListPrime.
import MarvellousPrimenNumber

def listPrime(numbers):
	primeNumbers = []
	for i in range (0,len(numbers)):
		if(MarvellousPrimenNumber.checkPrime(numbers[i])):
			primeNumbers.append(numbers[i])
	return primeNumbers


def sumlist(numbers):
	result = 0
	for i in range(0,len(numbers)):
		result = result + numbers[i]
	return result
	

def main():
	numbers = []
	value = int(input("Number of elements : "))
	for i in range(value):
		no1 = int(input("Enter number : "))
		numbers.append(no1)
	print("List of all elements is :  ", numbers)
	primeNumbers = listPrime(numbers)
	print("prime numbers are : ",primeNumbers)
	ans = sumlist(primeNumbers)
	print("Summation of all prime numbers is : ", ans)



if __name__ == "__main__":
	main()