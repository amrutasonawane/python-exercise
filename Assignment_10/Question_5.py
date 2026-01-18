#.Write a program which accepts one number and prints all odd numbers till that number.
def checkOdd(no1) :
	result = []
	for i in range(1,no1+1):
		if(i % 2) == 1:
			result.append(i)
	return result

def main():
	value1 = int(input("Input number : "))
	result = checkOdd(value1)
	print("Odd number are : ", result)

if __name__ == "__main__":
	main()