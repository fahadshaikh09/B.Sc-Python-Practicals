# Write a recursive function to print the factorial for a given number.

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n - 1)

def main():
	n = int(input("Enter number to find Factorial : "))

	fact = factorial(n)

	print("%d! = %d" % (n, fact) )

main()