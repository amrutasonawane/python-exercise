from functools import reduce

def CheckPrime(number):
	for i in range(2,(number//2)+1):
		if(number % i) == 0 :
				return None
	return number

def multiplication(no1):
	return no1 * 2

def checkMax(no1,no2):
	if(no1 > no2):
		return no1
	else:
		return no2

def main():
	data = []
	value = int(input("Enter numner of elements : "))
	for i in range(value):
		number = int(input("Enter element : "))
		data.append(number)
	print("Entered list is: ",data)
	fdata = list(filter(CheckPrime,data))
	print("List of prime number is : ",fdata)

	mdata = list(map(multiplication,fdata))
	print("mdata list is : ",mdata)

	result = reduce(checkMax,mdata)
	print("Greater number in list is : ",result)


if __name__ == "__main__":
	main()