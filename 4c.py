# Write a Python program to clone or copy a list

def input_list(count):
	#function to take list from user as input 
	a = list()
	while count != 0:
		elem = int(input("Enter Number : "))
		a.append(elem)
		count -= 1

	return a

def copy(l):
	#new empty list
	n = list()

	#iterate over list and append elements in new list
	for i in l:
		n.append(i)
	return n

def main():
	count = int(input("Enter Count for list : "))
	l = input_list(count)

	new = copy(l)

	print("Old List : ")
	print(l)

	print ("New list : ")
	print(new)

main()