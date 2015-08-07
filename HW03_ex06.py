#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
################################################################################
# Exercise 1
# When you submit only include your final function: compare
def compare(x,y):
#comparing x and y to return 1 if x>y, 0 if they are equal and -1 if x<y
	if (x>y):		
#		print("1")
		return 1
	if (x==y):
#		print("0")
		return 0
	if (x<y):
#		print("-1")
		return -1

################################################################################
# Exercise 2
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share here.

def hypotenuse(side1, side2):
#calculating square of sides
	side1_square=(side1**2.0)
	side2_square=(side2**2.0)
#calculating hypotenuse by taking the sqrt of sum of squares if sides
	hypotenuse=(side1_square+side2_square)**(1/2.0)
#	print hypotenuse
	return hypotenuse

################################################################################
# Exercise 3
# When you submit only include your final function: is_between

def is_between(x,y,z):
#comparing x, y and z to determine if y is between x and y
	if (x<=y and y<=z):
#		print "true"
		return True
	else:
#		print"false"
		return False
		
###############################################################################
# Exercise 6
# When you submit only include your final function: is_palindrome

def is_palindrome(string):
#reversing the string to compare with original string and determine if its a palindrome
	reverse_string=string[::-1]
	if (string==reverse_string):
#		print "true"
		return True
	else:
#		print "false"
		return False
		
################################################################################
# Exercise 7
# When you submit only include your final function: is_power
def is_power(a,b):
#determining is_power based on definition
	interim=a/b
	if (a%b==0 and interim%b==0):
#		print "true"
		return True
	else:
#		print "false"
		return False
		
	
	





################################################################################
def main():
#"""Your functions will be called within this function."""
############################################################################
# Use this space temporarily to call functions in development:
	print("Hello World!")
    ############################################################################
    # Uncomment the below to test and before commiting:
    # # Exercise 1
    #print compare(1,1)
    #print compare(1,2)
    #print compare(2,1)
    # # Exercise 2
    #print hypotenuse(1,1)
    #print hypotenuse(3,4)
    #print hypotenuse(1.2,12)
    # # Exercise 3
	#print is_between(1,2,3)
	#print is_between(2,1,3)
	#print is_between(3,1,2)
	#print is_between(1,1,2)
    # # Exercise 6
	#print is_palindrome("Python")
	#print is_palindrome("evitative")
	#print is_palindrome("sememes")
	#print is_palindrome("oooooooooooo")
    # # Exercise 7
	#print is_power(28,3)
	#print is_power(27,3)
	#print is_power(248832,12)
	#print is_power(248844,12)


if __name__ == "__main__":
    main()