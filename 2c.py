# Define a procedurehistogram() that takes a list of integers and prints a histogram to the screen. For example, 
# histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(l):
	# str multipled by any integer repeats the str that many times
	for i in l:
		print("*" * i)

def main():
	count = int(input("Enter count of numbers : "))

	# create empty list (array)
	l = list()

	while count>0:
		n = int(input("Enter number : "))
		# list.append method appends the elemnt in last of list
		l.append(n)

		count -= 1
	
	print("You Entered List :")
	print(l)

	histogram(l)

main()