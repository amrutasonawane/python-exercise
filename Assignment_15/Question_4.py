#Write a lambda function using reduce which accepts a list of numbers and returns the addition of all elements
from functools import reduce

numbers = [1,4,6,7,8,2,2]
print("Original list of numbers is : ",numbers)

addition = reduce((lambda no1,no2 : no1 + no2),numbers)
print("Addition of allbaove numbers is : ", addition)