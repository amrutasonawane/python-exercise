import sys
import os

def checkWordFrequesncy(words,chckString):
	counter = 0
	for word in words:
		if(word.lower() == chckString.lower()):
			counter = counter + 1
	return counter


def main():
	fileName = sys.argv[1]
	checkString = sys.argv[2]
	if(os.path.exists(fileName)):
		fobj = open(fileName,"r")
		fileContent = fobj.read()
		words = fileContent.split()
		occurences = checkWordFrequesncy(words,checkString)
		print(f"Occurence of given word in given file is : {occurences}")
		fobj.close()
	else:
		print("Given file is not present")
	
if __name__ == "__main__":
	main()