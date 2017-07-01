# Take a list, say for example this one:
# a=[1,1,2,3,5,8,13,21,34,55,89]
# and write a program that prints out all the elements of the list that are less than 5

def main():
	count = int(input("Enter Number of elements : "))

	# create empty list a
	a = list()

	#taking all elements from user
	while count > 0:
		elem = int(input("Enter Number : "))
		a.append(elem)
		count -= 1

	#iterate over list 'a' using for loop
	for i in a:
		if i < 5:
			print(i)

main()