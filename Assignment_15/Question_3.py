#Write a lambda function using filter which accepts a list of numbers and returns a list of odd num
numbers = [12,14,15,17,18,19,22,23,26]
print("Original numbers in the list is : ",numbers)
oddNumbers = list(filter((lambda no1 : no1%2 !=0),numbers))
print("List of Odd number is : ",oddNumbers)