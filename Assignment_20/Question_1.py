import threading
def getEven():
	for i in range(1,11):
		if i % 2 == 0:
			print(i)

def getOdd():
	limit = 10
	for i in range(1,11):
		if i % 2 != 0:
			print(i)

def main():
	t1 = threading.Thread(target=getEven)
	t1.start()

	t2 = threading.Thread(target=getOdd)
	t2.start()

	t1.join()
	t2.join()

	print("End of main")

if __name__ == "__main__":
	main()