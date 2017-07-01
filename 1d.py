# Write a function that reverses the user defined value

#function to take integer n as input and return revered number
def reverse(n):
	rev = 0

	while n != 0:
		#finding last digit
		last_digit = n % 10
		rev = (rev * 10) + last_digit
		# dividing by 10 to remove last digit
		n = n // 10

	return rev

def main():
	n = input("Enter a Number : ")
	#typecast to int
	n = int(n)

	rev = reverse(n)
	print("Reverse of %d Number is %d" % (n, rev) ) 

main()