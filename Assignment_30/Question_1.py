# Count Lines in a File
import sys
import os

def fileStatics(fileName):
	lineCount = 0
	file = open(fileName,"r")
	print(file)
	for line in file:
		lineCount = lineCount + 1
	return lineCount

def main():
	fileName = sys.argv[1]
	if(os.path.exists(fileName)):
		lineCount = fileStatics(fileName)
		print("Number of lines in a file are : ",lineCount)
	else:
		print("Given file is not exists")

if __name__ == "__main__":
	main()
