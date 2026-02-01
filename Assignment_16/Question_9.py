#Write a program which display first 10 even numbers
def displayEven():
	for i in range(2,20+1):
		if(i % 2 == 0):
			print(i)

def main():
	displayEven()

if __name__ == "__main__":
	main()
	
