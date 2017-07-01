# Write a program to generate the Fibonacci series.

count = input("Enter a Number : ")

#typecast to int
count = int(count)

a=1
b=0

while count>0:
	c = a+b
	print(c)
	a,b = b,c # a<-b and b<-c

	count = count - 1