# Write a program which accept one number and prints that many number starting from 1
def printNumber(no1):
	result = []
	for i in range(1,no1+1):
		result.append(i)
	return result

def main():
	value1 = int(input("Enter a number : "))
	numbers = printNumber(value1)
	print(numbers)

if __name__ == "__main__":
	main()