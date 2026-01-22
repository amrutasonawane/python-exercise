#Write a program which give factorial of given number
def factorial(no1):
	factors = []
	for i in range(1, no1 + 1) :
		if(no1 % i) == 0 :
			factors.append(i)
	return factors

def main():
	value = int (input("Enter a number : "))
	factors = factorial(value)
	print(factors)

if __name__ == "__main__":
	main()