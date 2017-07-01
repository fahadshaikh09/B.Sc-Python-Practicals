# Write a program that takes two lists and returns True if they have at least one common member.

def input_list(count):
	a = list()
	while count != 0:
		elem = int(input("Enter Number : "))
		a.append(elem)
		count -= 1

	return a

def check(list1,  list2):
	#iterate over list1 and checking elements in list2
	for i in list1:
		if i in list2:
			return True
	return False

def main():
	count1 = int(input("Enter Count for list 1: "))
	list1 = input_list(count1)

	count2 = int(input("Enter Count for list 2: "))
	list2 = input_list(count2)	

	if check(list1, list2):
		print("Both List have at least 1 common element")
	else:
		print("List dont have any common element")

main()