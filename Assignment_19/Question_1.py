#Write a program which contains one lambda function which accepts one parameter and return power

getSquare = lambda no1 : no1 ** 2

def main():
	value = int(input("Enter number : "))
	result = getSquare(value)
	print("Square if entered number is:",result)

if __name__ == "__main__":
	main()