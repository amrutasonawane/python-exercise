#Copy File Contents into Another File
import os
import sys

def copyFile(fileName1, fileName2):
	print("Started copying file")
	fobj = open(fileName1, "r")
	data = fobj.read()
	fobj1 = open(fileName2,"w")
	fobj1.write(data)
	print("done")

def main():
	fileName1 = sys.argv[1]
	fileName2 = sys.argv[2]
	if(os.path.exists(fileName1)):
		copyFile(fileName1,fileName2)
	else:
		print("File not present")

if __name__ == "__main__" :
	main()