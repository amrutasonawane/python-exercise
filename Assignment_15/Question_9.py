#Write a lambda function using reduc which accepts a list of numbers and returns the product of all elements.
from functools import reduce
data = [2,5,8,2,7,9,10]
print("Original data is : ",data)
reduceData = reduce((lambda no1, no2 : no1 *no2),data)
print("multiplication of all nubres is : ", reduceData)
