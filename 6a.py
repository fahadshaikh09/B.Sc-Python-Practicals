# Write a Python program to read an entire text file.

def main():
	#opening file in read mode
	f = open("sample_text.txt", "r")
	
	#f.read() method reads the complete text file
	file_content = f.read()

	print(file_content)

	#close the file
	f.close()

main()