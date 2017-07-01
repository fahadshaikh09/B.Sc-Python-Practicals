# Write a Python program to append text to a file and display the text.

def main():
	#opening file in append mode
	f = open("sample_text.txt", "a")
	f.write("Some more text")
	f.close()

	#opening file in read mode
	f = open("sample_text.txt", "r")
	file_content = f.read()
	f.close()	
	
	print(file_content)
	
main()