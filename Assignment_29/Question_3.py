#Copy File Contents into a New File (accept filename from commnad lime)
import os
import sys
def main():
	fileName = sys.argv[1]
	isfileExist = os.path.exists(fileName)
	if(isfileExist):
		print(f"file {fileName} is present in curent directory")
		fobj = open(fileName,"r")
		data = fobj.read()
		fobj1 = open("Hello.txt", "w")
		fobj1.write(data)
		fobj.close()
		fobj1.close()
	else:
		print("Given file does not presnet in current directory")

if __name__ == "__main__":
	main()