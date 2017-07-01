# Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.

def input_list(count):

	a = list()
	while count != 0:
		elem = int(input("Enter Number : "))
		a.append(elem)
		count -= 1

	return a

def main():
	count = int(input("Enter Count for list : "))

	if count<6:
		print("Enter Count greater than or equal to 6")
	else:
		l = input_list(count)
		print("inputed List : ")
		print(l)

		del l[0]
		
		# after removing 0th element, index of 2nd element will be 1
		del l[1]

		# after removing 0th, 1st element, index of 4th element will be 2
		del l[2]
		
		# after removing 0th, 1st, 4th element, index of 5th element will be 2
		del l[2]

		print("After removing 0th, 2nd, 4th and 5th Element")
		print(l)

main()