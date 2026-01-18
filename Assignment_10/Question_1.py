
#1. Write a program which accepts one number and prints multiplication table of that number.
#Input: 4 Output:
#4 8 12 16 20 24 28 32 36 40
def multiplicationTable(no1) :
	result = []
	for i in range(1,11) : 
		result.append(no1 * i)
	return result


def main() :
	table = multiplicationTable(4)
	print("Multiplication table for given number is : ", table)

if __name__ == "__main__":
	main()