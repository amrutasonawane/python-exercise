#Write a program which accept number and checks wheather it is perfect number or not

def checkPerfect(no1):
	sum = 0
	for i in range(1,(no1 // 2)+1):
		if(no1 % i) == 0 :
			sum = sum +i
	return sum

def main():
	value = int(input("Enter a number : "))
	result = checkPerfect(value)
	if(result == value):
		print("Given number is perfect number",result)
	else:
			print("Given number is not perfect number",result)

if __name__=="__main__":
	main()