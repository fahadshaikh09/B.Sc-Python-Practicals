# Write a Python program to sum all the items in a dictionary.

def main():
	d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

	#sum initialy 0
	s = 0
	
	#iterating over dictionary to find sum of values 
	for key, value in d.items():
		s = s + value

	print("Sum of Values of Dictionary is : %d" % s)

main()