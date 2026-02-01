import threading
def countDigit (inputString):
	count = 0
	for i in range (len(inputString)):
		if inputString[i].isdigit():
			count= count+1
	print("Count of Digits in given string is : ",count)

def countCapital (inputString):
	count = 0
	for i in range (len(inputString)):
		if inputString[i].isupper():
			count= count+1
	print("Count of Capital letters in given string is : ",count)

def countSmall (inputString):
	count = 0
	for i in range (len(inputString)):
		if inputString[i].islower():
			count= count+1
	print("Count of lower case character are : ",count)


def main():
	inputString = input("Enter a string : ")
	small = threading.Thread(target=countSmall,args=(inputString,))
	Capital = threading.Thread(target=countCapital,args=(inputString,))
	Digit = threading.Thread(target=countDigit,args=(inputString,))
	small.start()
	small.join()
	print("Thread id and thread name is", small.name, small.ident)

	Capital.start()
	Capital.join()
	print("Thread id and thread name is", Capital.name, Capital.ident)

	Digit.start()
	Digit.join()
	print("Thread id and thread name is", Digit.name, Digit.ident)

	print("End of main")

if __name__ == "__main__":
	main()