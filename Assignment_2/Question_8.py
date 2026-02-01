#8. Predict the output:
#x = input("Enter number: ") print(type(x)) Explain the reason.

x = input("Enter number : ")
print(type(x))

#Enter number : 20
#<class 'str'>

#Ans - input() function always reads the user's entry as a string, 
#regardless of what is typed. Even if you enter 10, Python stores it as the text "10"