# Write a program which accept numbers from user and store it into List. Return addition of all elements from that List.
def addition(numberlist):
	result = 0
	for i in range(1,len(numberlist)+1):
		result = result + i
	return result

def main():
	numbers = []
	value = int(input("How many numbers do you want to add in list : "))
	for i in range(value):
		data = input("Enter number : ")
		numbers.append(data)

	print("List of element from list is : ",numbers)
	print("Addition of numbers from list is : ",addition(numbers))

if __name__ == "__main__":
	main()