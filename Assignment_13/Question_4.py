#Write a program which accepts one number and prints binary equivalent \\

def toBinary(value):
	binary = ""
	while(value>0):
		binary = str(value % 2)+binary
		print(binary)
		value = value // 2
	return binary


def main():
	value = int(input("Enter a number : "))
	result = toBinary(value)
	print("binary if given number is : ",result)

if __name__=="__main__":
	main()