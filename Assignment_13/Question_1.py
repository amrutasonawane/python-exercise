# Write a prgram which accept length and width of rectangle and prints area
def areaRect(length, width):
	return  length * width

def main():
	value1 = int(input("Enter length of rectangle : "))
	value2 = int(input("Enter width of rectangle : "))
	area = areaRect(length=value1,width=value2)
	print("Area of rectangle is : ",area)

if __name__=="__main__":
	main()