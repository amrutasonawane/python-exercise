#Write a lambda function using reduce which accepts a list of numbers and returns the maximum element
from functools import reduce
numbers = [10,20,30,40,50,60]
print("Original numbers are : ",numbers)
maxElement = reduce(lambda no1,no2 : max(no1,no2),numbers)
print("Max number is : ",maxElement)
