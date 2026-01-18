# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
#Input: 15
#Output: Divisible by 3 and 5
def checkDivisible(no1):
	checkDivisible = ""
	if(no1 % 3) == 0 and (no1 % 5) == 0:
		 checkDivisible = "Given number is divisible by 3 and 5"
	else:
			checkDivisible = "Not divisible by 3 or 5"
	return checkDivisible


def main():
	result = checkDivisible(45)
	print(result)

if __name__ == "__main__":
	main()