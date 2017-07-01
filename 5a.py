# Write a Python script to sort (ascending and descending) a dictionary by value

def main():
	# sample dictionary
	d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 0:-10}

	# as dictionary doesn't preserve order of elements,
	# hence convert dictionary into list of tuples

	data = d.items()

	#sorting data on the basis of value
	data_ascending = sorted(data, key=lambda x: x[1])

	#for sorting in descending order, add param reverse=True in sorted function
	data_descending = sorted(data, key=lambda x: x[1], reverse=True)
	
	print("Sorted Data (Ascending) : ")
	print(data_ascending)
	print("Sorted Data (Descending) : ")
	print(data_descending)

main()