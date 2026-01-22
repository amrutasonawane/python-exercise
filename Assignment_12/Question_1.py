#Write a program which accept one char from user and check weather ot is vowels or conmsonant
def checkVowels(char1):
	charset = ['a','e','i','o','u']
	if char1 in charset:
		print("It is a Vowel")
	else :
		print("It is a Consonant")


def main():
	char = input("Enter character : ").lower()
	checkVowels(char)
	

if __name__ == "__main__":
	main()