#---Create function to take two parameters and add them
#---Returns the sum of the two parameters
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

#---Create function to take two parameters and subtract the second from the first
#---Returns the difference of a - b
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

#---Create function to take two parameters and multiply them together
#---Return the product of the two parameters ==> a * b
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

#---Create function to take two parameters and divide the first by the second
#---Return the quotient created by ==> a / b
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b


#---Send text to the screen
print("Let's do some math with just functions!")

#---Create age variable using add(a,b) function
age = add(30, 5)
#---Create height variable using height(a,b) function
height = subtract(78, 4)
#---Create weight variable using weight(a,b) function
weight = multiply(90, 2)
#---Create iq variable using divide(a,b) function
iq = divide(100, 2)

#---Print text to screen
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway. 
print("Here is a puzzle.")

#---Create variable named what while also showing functions can be 
#-------placed as parameters within other functions
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#---Print text and variable what to screen
print("That becomes: ", what, "Can you do it by hand?")

