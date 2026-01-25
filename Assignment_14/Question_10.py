#Write a lambda function which accepts three numbers and returns largest num
largestNumber = lambda no1,no2,no3 : max(no1,no2,no3)


value1 = int(input("Enter first number : "))
value2 = int(input("Enter second number : "))
value3 = int(input("Enter third number : "))

print("Largest of 3 numbers is : ",largestNumber(value1,value2,value3))