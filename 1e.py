# Write a function to check the input value is Armstrong and also write the function for Palindrome.

def isArmstrong(n):
	#armstrong number is a number whose sum of cube of digits is the same number
	# 1^3 + 5^3 + 3^3 = 153

	copy = n

	#sum initially 0
	s = 0

	while n!=0:
		last_digit = n % 10
		# ** operator is use to find power 
		s = s + (last_digit ** 3)
		n = n // 10

	if s==copy:
		return True
	else:
		return False

def isPalindrome(s):
	rev = s[::-1]
	if rev==s:
		return True
	else:
		return False

def main():
	#input number to check armstrong number
	n = int(input("Enter number to check armstrong : "))

	if isArmstrong(n):
		print("%d is Armstrong number" % n)
	else:
		print("%d is not Armstrong number" % n)

	#input string to check palindrome
	s = input("Enter string to check palindrome : ")

	if isPalindrome(s):
		print("%s is Palindrome" % s)
	else:
		print("%s is not Palindrome" % s)

main()