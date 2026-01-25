#Write a lambda function using reduce which accepts a list of numbers and returns the minimum element.
from functools import reduce
numbers = [41,100,144,455,3,89,67]
print("Original numbers are : ",numbers)
minNumber = reduce(lambda no1,no2 : min(no1,no2),numbers)
print("Minimum number is : ",minNumber)
