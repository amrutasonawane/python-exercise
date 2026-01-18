#Write a program which accepts one number and prints count of digits in that number.
def giveCount(no1):
	return len(str(no1))


def main():
	value = int(input("Enter number : "))
	result = giveCount(value)
	print("Count of digit in given number is : ", result)
if __name__ == "__main__":
	main()