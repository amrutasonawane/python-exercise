#Write a lambda function using map which accepts a list of numbers and returns a list of squares of each num
numbers = [3,4,5,6,7,8]
print("Actual data is : ", numbers)

numberSquares = list(map(lambda a : a * a,numbers))
print("Squares of all numbers are : ",numberSquares)