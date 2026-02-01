#Write a program which accept one number and display below pattern

def displayPattern(num1):
	for i in range(num1,0,-1):
			print("* " * i)

def main():
	value = int(input("Enter number : "))
	displayPattern(value)

if __name__  == "__main__":
	main()