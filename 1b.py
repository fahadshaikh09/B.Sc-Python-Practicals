# Enter the number from the user and depending on whether the number is even or odd, print out an appropriate message to the user.

n = input("Enter a Number : ")

#typecast n from str to int
n = int(n)

# if number divided by 2 gives remainder 0 then its Even
if n%2==0:
	print("%d is Even" % n)
else:
	print("%d is Odd" % n)