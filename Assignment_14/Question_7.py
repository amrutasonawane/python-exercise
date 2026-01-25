#Write a lambda function which accepts one number and returns True if divisible by 5

divisibleNum = lambda no1 : no1 % 5 == 0

value = int(input("Enter number : "))
if(divisibleNum(value)):
	print("Given number is divisible by 5")
else:
	print("Given number is not divisible by 5")
