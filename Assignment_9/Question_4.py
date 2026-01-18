#4. Write a program which accepts one number and prints cube of that number.
def getCube(no1):
	return no1 * no1 * no1


def main():	
	result  = getCube(5)
	print("Cube of given number is : ",result)

if __name__ == "__main__":
	main()