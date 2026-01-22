# Write a program which accepts one number and checks whether it is palindrome or not.
def isPalindrome(no1):
	reverse = 0
	while(no1>0):
		last_digit = no1%10
		reverse = (reverse * 10) + last_digit
		no1 = no1 // 10
	return reverse

def main():
	givenNumber = int(input("Enter a number : "))
	reverseNumber = isPalindrome(givenNumber)
	if (givenNumber == reverseNumber):	
		print("Given number is palindrome")
	else:
		print("Given number is not palindrome")

if __name__ == "__main__":
	main()