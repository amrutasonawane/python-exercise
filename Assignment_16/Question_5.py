#Write a program which display 10 to 1 on screen

def displayNum(no1):
	for i in range(no1,0,-1):
		print(i)


def main():
	value = int(input("Enter number : "))
	displayNum(value)

if __name__ == "__main__":
	main()
