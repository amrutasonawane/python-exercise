
#Write a program which accepts one number and prints multiplication table of that number.

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