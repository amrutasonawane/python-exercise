# Display File Contents

import os
def main():
	fileName = input("Enter file name : ")
	if (os.path.exists(fileName)):
		fobj = open(fileName,"r")
		print("file open successfully")
		print("Here is the file content : ", fobj.read())
		fobj.close()
	else:
		print("File not exists")
if __name__ == "__main__":
	main()