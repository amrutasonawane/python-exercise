 #Display File Line by Line
import sys
import os

def main():
	fileName = sys.argv[1]
	if(os.path.exists(fileName)):
		fobj = open(fileName,"r")
		data =  fobj.read()
		print("content fromfile is following : \n",data)
	else:
		print("File not present")
if __name__ == "__main__":
	main()