#Write a program which accept marks and display grades
def checkGrade(marks):
	if(marks >= 75):
		return "Distinction"
	if(marks >= 60):
		return "First class"
	if(marks >= 50):
		return "Second class"
	if(marks < 50):
		return "Fail"

def main():
	marks = int(input("Enter marks : "))
	grade = checkGrade(marks)
	print(grade)


if __name__ == "__main__":
	main()