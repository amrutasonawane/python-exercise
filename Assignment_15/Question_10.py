#Write a lambda function using filter which accepts a list of numbers and returns the count of even number
numbers = [19,33,45,67,44,34,22,21,31,41]
print("List of original numbers is : ", numbers)
evenNumbers = list(filter((lambda no1 : no1%2 == 0),numbers))
countEven = len(evenNumbers)
print("Count of even  umbers in above list is : ", countEven)