import threading

def getEven(numbers):
	print(numbers)
	sumEven = 0
	evenList = []
	for i in range(0,len(numbers)):
		if(numbers[i] % 2) == 0:
			evenList.append(numbers[i])
			sumEven = sumEven + numbers[i]
	print("List of even number from list is :",evenList)
	print("Sum of even number is : ",sumEven)

def getOdd(numbers):
	sumOdd = 0
	oddList = []
	for i in range(0,len(numbers)):
		if(numbers[i] % 2) != 0:
			oddList.append(numbers[i])
			sumOdd = sumOdd + numbers[i]
	print("List of even number from list is : ",oddList)
	print("Sum of even number is : ",sumOdd)


def main():
	print("Enter in main")
	numbers = [3,5,2,8,24,56,78,98,33,42,41,51,57,79,56]
	print("Given list is : ",numbers)

	evenList = threading.Thread(target=getEven,args=(numbers,))
	oddList = threading.Thread(target=getOdd,args=(numbers,))

	evenList.start()
	oddList.start()

	evenList.join()
	oddList.join()

	print("Exit from main")



if __name__ == "__main__":
	main()