# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise

def isVowel(s):
	if len(s)!=1:
		print("Only String of length 1 is allowed")
		return None

	if s in "aeiou":
		return True
	else:
		return False

def main():
	s = input("Enter Char (Length 1) : ")

	isV = isVowel(s)

	if isV==True:
		print("%s is a vowel" % s)
	elif isV==False:
		print("%s is not a vowel" % s)
	
main()