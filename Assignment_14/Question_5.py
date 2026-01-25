#Write a lambda function which accepts one number and returns True if number is even else False.
checkEven  = lambda no1 : no1%2 == 0


value = int(input("Enter number : "))
if(checkEven(value)):
	print("Given number is even")
else:
	print("Given number is odd")