#Write a program which accept name from user and display length of name

def displayLength(name):
	print("Length of entered string is : ",len(name))

def main():
	value = input("Enter name :")
	displayLength(value)

if __name__ == "__main__":
	main()
