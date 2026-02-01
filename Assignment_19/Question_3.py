#34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#[76, 89, 86, 90, 70]
#[86, 99, 96, 100, 80] 
#6538752000

from functools import reduce
def filteNum(no1):
	if no1 >= 70 and no1 <=90:
		return no1

def increment(no1):
	return no1 + 10

def multiplication(no1,no2):
	return no1 * no2

def main():
	value = int(input("Enter number of elements : "))
	data = []
	for i in range(value):
		number = int(input("Enter element : "))
		data.append(number)

	print("Input list is : ", data)
	fdata = list(filter(filteNum,data))
	print("filter data is : ",fdata)

	mdata = list(map(increment,fdata))
	print("data after map is :",mdata)

	result = 	reduce(multiplication,mdata)
	print("Result of multiplication is : ",result)


if __name__ == "__main__":
	main()