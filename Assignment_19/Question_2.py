#Write a program which contains one lambda function which accepts two parameters and return its multi
multiplication = lambda no1,no2 : no1 * no2

def main():
	no1 =  int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))
	ans = multiplication(no1,no2)
	print("Multiplication of 2 number is : ", ans)

if __name__ == "__main__":
	main()