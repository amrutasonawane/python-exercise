#Write a program which accept N numbers from user and store it into List. Return Min number from that List
def checkMax(allNumbers):
	result = allNumbers[0]
	for i in range(0,len(allNumbers)):
		if(allNumbers[i] < result):
			result = allNumbers[i]
	return result

def main():
	numbers = []
	total = int(input("How many element you want to add : "))
	for i in range (total):
		data = int(input("Enter number : "))
		numbers.append(data)
	print("Number ofelements from list is : ",numbers)
	maxNumber = checkMax(numbers)
	print("Min number is : ",maxNumber)

if __name__ == "__main__":
	main()