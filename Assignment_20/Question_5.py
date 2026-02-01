import threading

def displayNum():
	for i in range(1,50+1):
		print(i)

def displayNumReverse():
	for i in range(50,0,-1):
		print(i)

def main():
	print("Start of main")
	display = threading.Thread(target=displayNum)
	display1 = threading.Thread(target=displayNumReverse)

	display.start()
	display1.start()

	display.join()
	display1.join()

	print("End of main")

if __name__ == "__main__":
	main()