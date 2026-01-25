#Write a lambda function which accepts two numbers and returns max num.
maxNumber  = lambda no1,no2 : max(no1,no2)

value1 = int(input("Enter first number : "))
value2 = int(input("Enter second number : "))
print("Greater number is : ", maxNumber(value1,value2))
