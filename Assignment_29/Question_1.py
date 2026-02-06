#Check File Exists in Current Directory
import os

def main():
	fileName = input("Enter file name : ")
	isFileExist = os.path.exists(fileName)
	if(isFileExist):	
		open(fileName,"r")
		print("File get successfully open")
	else:
		print("File not exist in current directory")
if __name__ == "__main__":
		main()