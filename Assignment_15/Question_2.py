# Write a lambda function using filter, accepts a list of numbers and returns a list of even num
numbers = [4,8,12,13,17,19,22]
print("List of original number is : ", numbers)
evenNumbers = list(filter((lambda no1 : no1%2 == 0),numbers))
print("Listof even number is : ", evenNumbers)