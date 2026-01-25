# Write a lambda function which accepts one number and returns square of that number.
square = lambda a : a * a

value = int(input("Enter number : "))
print("Square of given number is : ", square(value))