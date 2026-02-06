#Count Words in a File
import sys
import os
def countWords(fileContent):
	count = 0
	fileContent = fileContent.split()
	for words in fileContent:
			count = count +1
	return count

def main():
	fileName = sys.argv[1]
	if(os.path.exists(fileName)):
		fobj = open(fileName,"r")
		data = fobj.read()
		wordCount = countWords(data)
		print("Count of words in given file is : ",wordCount)
		

if __name__ == "__main__":
	main()