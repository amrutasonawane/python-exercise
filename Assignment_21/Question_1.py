import threading

def checkPrime(value):
	for i in range(2,(value//2)+1):
		if (value % i) == 0:
			return False
	return True

def checkNotPrime(value):
	for i in range(2,(value//2)+1):
		if (value % i) == 0:
			return True
	return False

def displayPrime(numbers):	
	print("List of prime is :")
	for i in range (2,len(numbers)):
		if(checkPrime(numbers[i])):
			print(numbers[i])
	

def displayNotPrime(numbers):	
	print("List of Nonprime is :")
	for i in range (2,len(numbers)):
		if(checkNotPrime(numbers[i])):
			print(numbers[i])

def main():
	print("Start of main")
	data = [12,11,5,8,15,17,19,11,7,45,34,32,67,12,9]
	prime = threading.Thread(target=displayPrime,args=(data,))
	nonPrime = threading.Thread(target=displayNotPrime,args=(data,))

	prime.start()
	nonPrime.start()

	prime.join()
	nonPrime.join()	
	
	print("End of main")


if __name__ == "__main__":
	main()