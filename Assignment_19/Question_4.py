from functools import reduce

def checkEven(no1):
	if no1%2 == 0:
		return no1

def getSquare(no1):
	return no1 * no1

def sum(no1,no2):
	return no1 + no2

def main():
	value = int(input("Enter number ofelements : "))
	data = []
	for i in range(value):
		number = int(input("Enter element : "))
		data.append(number)
	print("Input list is : ",data)
	fdata = list(filter(checkEven,data))
	print("Filter data is : ",fdata)
	
	mdata = list(map(getSquare,fdata))
	print("Mapped data is : ",mdata)

	result = reduce(sum,mdata)
	print("Summation of all number is : ",result)






if __name__ == "__main__":
	main()