#Write a program which accepts one number and prints sum of first N natural numbers.

def summation(no1):
	result = 0
	#for i in range(no1,0,-1):
	for i in range(1,no1+1):
		result = result + i
	return result

def main() : 
	result = summation(5)
	print("Summation of first N natural number is : ",result)

if __name__ == "__main__" :
	main()