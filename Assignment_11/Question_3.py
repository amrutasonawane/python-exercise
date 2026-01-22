#Write a program which accepts one number and prints sum of digits.
#Input: 123
#Output: 6
def sumOfDigit(no1):	
	total = 0
	for digit in str(no1):
		total = total + int(digit)
	return total

def main():
	value = int(input("Enter number : "))
	result = sumOfDigit(value)
	print("Summation of all digit in a number is : ",result)

if __name__ == "__main__":
	main()
