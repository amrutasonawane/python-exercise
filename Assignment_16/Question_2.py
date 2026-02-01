#Write a program which contains one fun -> which accept one parameter as number. If number is display "Even number" else "Odd number" 
def checkNum(no1):
	if(no1%2 == 0):
		print("Given number is even")
	else:
		print("Given number is odd")

def main():
	value = int(input("Enter number : "))
	checkNum(value)

if  __name__ == "__main__":
	main()

