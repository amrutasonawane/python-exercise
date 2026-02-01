#10: Design a Python application that creates 2 threads
#Thread 1 should compute the sum of elements from a list.
#Thread 2 should compute the product of elements from the same list.
#Return the results to the main thread and display them.
import threading
def sumNumbers(numbers):
	sum = 0
	for i in range(len(numbers)):
		sum = sum + numbers[i]
	print	(sum)
	return sum


def mult(numbers):
	mult = 1
	for i in range(len(numbers)):
		mult = mult * numbers[i]
	print(mult)
	return mult


def main():
	numbers = [2,3,4]
	sumThread = threading.Thread(target=sumNumbers,args=[numbers,])
	multThread = threading.Thread(target=mult,args=[numbers,])
	
	sumThread.start()
	multThread.start()

	sumThread.join()
	multThread.join()

if __name__ == "__main__":
	main()


