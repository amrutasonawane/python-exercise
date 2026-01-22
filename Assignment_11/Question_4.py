#4. Write a program which accepts one number and prints reverse of that number.
#Input: 123
#Output: 321
def reverseNumber(no1):
	reverse = 0
	while(no1>0):
		last_digit = no1 % 10
		reverse = (reverse * 10)+last_digit
		print(reverse)
		no1 = no1//10
		print(no1)
	return reverse

def main():
	value = int(input("Enter a number : "))
	result = reverseNumber(value)
	print("Reverse number is : ",result)

if __name__ == "__main__":
	main()