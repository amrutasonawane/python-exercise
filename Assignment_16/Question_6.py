#Write a program which accept number and check whether that number is +ve or -ve or 0

def checkNumber(value):
	if(value == 0):
		print("Entered number is 0")
	elif(value < 0):
		print("Entered number in Negative")
	else:
		print("Entered number is Positive")

def main():
	value = int(input("Enter number : "))
	checkNumber(value)

if __name__ == "__main__":
	main()
