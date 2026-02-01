def displayPattern(num1):
	for i in range(1,num1+1):
		for j in range (1,i+1):
			print(j,end = " ")
		print()

def main():
	value = int(input("Enter number : "))
	displayPattern(value)

if __name__  == "__main__":
	main()