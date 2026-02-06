#Search a Word in File

import os
import sys
def checkWord(fileName, givenString):
	fobj = open(fileName,"r")
	content = fobj.read()
	words = content.split()
	for word in words :
		if (givenString == word):
			return True
	return False

def main():
	fileName = sys.argv[1]
	word = sys.argv[2]
	if(os.path.exists(fileName)):
		isWordPresent = checkWord(fileName,word)
		if(isWordPresent):	
			print("Given word is present in file")
		else:
			print("Given word is not present in file")
	else:
		print("file not present")

if __name__ == "__main__":
	main()