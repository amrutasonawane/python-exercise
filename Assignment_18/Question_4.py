#Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
def calculateDigit(numbers, no1):
	result = 0
	for i in range(0,len(numbers)):
		if numbers[i] == no1:
			result= result+1
	return result

def main():
	numbers = []
	value = int(input("Enter how many element you want to add : "))
	for i in range(value):
		num = int(input("Enter number : "))
		numbers.append(num)
	print(numbers)
	num1 = int(input("Enter which number you wants to search : "))
	result = calculateDigit(numbers,num1)
	if(result > 0):
		print("Occurance of digit under given list is : ", result)
	else:
		print("Entered numer is not in list")

if __name__ == "__main__":
	main()