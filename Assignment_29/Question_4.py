 #Compare Two Files (Command Line)
import filecmp
import sys
import os
def main():
	fileName_1 = sys.argv[1]
	fileName_2 = sys.argv[2]
	if(os.path.exists(fileName_1) and os.path.exists(fileName_2)):
		if(filecmp.cmp(fileName_1,fileName_2)):
			print("files are identitical")
		else:	
			print("files are different")
	else:
		print("File not present")

if __name__ == "__main__":
	main()