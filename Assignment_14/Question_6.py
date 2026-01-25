#Write a lambda function which accepts one number and returns True if number is odd 
checkOdd = lambda no1: no1 % 2 != 0

value = int(input("Enter number : "))
if(checkOdd(value)):
	print("Given number is odd")
else:
	print("Given number is Even")
