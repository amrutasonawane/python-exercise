# Accept radius of circle and print area of circle
import math

def areaCircle(radius):
	pi = 3.14
	return  math.pi * (radius ** 2)

def main():
	radius = int(input("Enter radius of circle : "))
	area = areaCircle(radius)
	print("Area of Circle is : ",area)

if __name__=="__main__":
	main()
