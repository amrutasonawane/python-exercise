#Write a program which accept number from user and print that number of Input: 5 Output : *
def display(no1):
	print("*  " * no1)

def main():
	value = int(input("Enter number : "))
	display(value)

if __name__ == "__main__":
	main()
