# Write a program which accept one number and prints that many number starting from that number 5,4,3,2,1

def printReverseNumber(no1):
	result = []
	for i in range(no1,0,-1):
		result.append(i)
	return result

def main():
	value1 = int(input("Enter a number : "))
	numbers = printReverseNumber(value1)
	print(numbers)

if __name__ == "__main__":
	main()