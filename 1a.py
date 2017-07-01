# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter Name : ")
age = input("Enter Age : ")

#typecase str to int
age = int(age)

curr_year = 2017
age_diff = 100 - age

print("Hello %s, You will turn 100 in the year %d" % (name, curr_year+age_diff) )