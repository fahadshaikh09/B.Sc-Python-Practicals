# Write a Python program to read last n lines of a file.

def main():
	#opening file in read mode
	f = open("sample_text.txt", "r")
	file_content_lines = f.readlines()

	#assume last 4 lines to be read
	n = 4

	#starts from last line, go till n lines, in reverse order
	last_n_lines = file_content_lines[-1:-n-1:-1]

	print(last_n_lines)

	f.close()

main()