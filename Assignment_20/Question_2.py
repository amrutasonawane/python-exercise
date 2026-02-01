import threading
def getEvenFactor(no1):
	evenSum = 0
	evenFactor = []
	for i in range(1, no1 + 1):
		if no1 % i == 0 and i % 2 == 0:
			evenFactor.append(i)
			evenSum = evenSum + i
	print("Factors of given number is : ", evenFactor)
	print("Sum of all Even factors is : ", evenSum)

def getOddFactor(no1):
	oddSum = 0
	oddFactor = []
	for i in range(1, no1 + 1):
		if no1 % i == 0 and i % 2 != 0:
			oddFactor.append(i)
			oddSum = oddSum + i
	print("Factors of given number is : ", oddFactor)
	print("Sum of all Odd factors is : ", oddSum)


def main():
	print("Enter in main")
	Value = int(input("Enter number : "))
	evenFactor = threading.Thread(target=getEvenFactor, args=(Value,))
	oddFactor = threading.Thread(target=getOddFactor, args=(Value,))
	evenFactor.start()
	oddFactor.start()
	evenFactor.join()
	oddFactor.join()
	print("End of main")

if(__name__ == "__main__"):
	main()