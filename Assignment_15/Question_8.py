#Write a lambda function using filter which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.
data = [21,33,45,66,78,30,35,22,95,100]
print("Original data is : ", data)
filterdata = list(filter((lambda no1 : no1%3==0 and no1%5==0),data))
print("List of number divisible by 3 and 5 is : ",filterdata)