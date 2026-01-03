import sys
#6. Write a program to display:
#Data type
#Memory address
#Size in bytes
#of a variable entered by the user.

random = input("Enter any value, I will tell you data type, memory address and size in bytes ")
print("Data type of given value is : ",type(random))
print("memory address of given value is : ",id(random))
print("Size in bytes of given value is : ",sys.getsizeof(random))

