import threading

def displayMax(numbers):
	maxNumber = 0
	for i in range (len(numbers)):
		if(numbers[i] > maxNumber):
				maxNumber = numbers[i]
	print("Largest number from list is : ",maxNumber)

def displayMin(numbers):
	minNumber = numbers[0]
	for i in range (len(numbers)):
		if(numbers[i] < minNumber):
				minNumber = numbers[i]
	print("Minimum number from list is : ",minNumber)

def main():
	numbers = []
	value = int(input("Enter number of elements : "))
	for i in range(value):
		num  = int(input("Enter number : "))
		numbers.append(num)
	print("Input list is : ",numbers)
	maximum = threading.Thread(target=displayMax,args=(numbers,))

	minimum = threading.Thread(target=displayMin,args=(numbers,))
	maximum.start()
	minimum.start()

	maximum.join()
	minimum.join()

	print("End of main")


if __name__ == "__main__":
	main()