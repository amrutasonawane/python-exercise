# Write a lambda function which accepts one number and returns cube of that number.
cube  = lambda no1 : no1 ** 3


value = int(input("Enter number : "))
print("Cube of given number is : ", cube(value))