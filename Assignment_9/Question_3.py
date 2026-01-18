#3. Write a program which accepts one number and prints square of that number.
#Input: 5
#Output: 25
def getSquare(no1):
	return no1 * no1

def main():
	value = 5
	result = getSquare(value)
	print("Square of given number is : ",result)

if __name__ == "__main__":
	main()
