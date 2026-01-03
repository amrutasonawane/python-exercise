#2. What is the difference between:
#a= 10
#b = 10 and a =[10] b = [10] Explain using id().

a=10
b=10
print(id(a))
print(id(b))
# Output is - 4498016504    4498016504
#When we assign 10 to a and then 10 to b, python doesnt waste memory by creating two objects for 10, 
#its simply assign 2 diffrent variable to same object hence memory address for both is same


a=[10]
b=[20]

print(id(a))
print(id(b))
# Output is 4475222144   4475062784
# when we add [] it menas it is list data type and list oin mutable in python, every time when we write [], 
# python allocates new block of memory


