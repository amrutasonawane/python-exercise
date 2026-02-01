#Write a program which accept one number and display pattern
def displayPattern(no1):
	for i in range (no1):
		for j in range (no1):
			print("*", end=" ")
		print()


def main():
	value = int(input("Enter number : "))
	displayPattern(value)

if __name__  == "__main__":
	main()