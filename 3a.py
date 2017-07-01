# A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.

def isPangram(s):
	for alphabet in "abcdefghijklmnopqrstuvwxyz":
		# if any alphabet is not present in string then return False
		if alphabet not in s:
			return False

	# if loop completes then return True
	return True


def main():
	s = input("Enter a string to check pangram : ")

	if isPangram(s):
		print("String '%s' is Pangram" % s)
	else:
		print("String '%s' is not Pangram" % s)

main()