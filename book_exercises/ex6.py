#--- Create a variable holding a number
types_of_people = 10
#--- Create a variable holding an f-string
x = f"There are {types_of_people} types of people."

#--- Create a variable holding a string
binary = "binary"
#--- Create a variable holding a string
do_not = "don't"
#--- Create a variable holding an f-string
y = f"Those who know {binary} and those who {do_not}."

#--- Print f-string from variable x to the screen
print(x)
#--- Print f-string from variable y to the screen
print(y)

#--- Print out a new f-string to show that an f-string 
#------ can be placed inside an f-string
print(f"I said: {x}")
#--- Print out a new f-string to show that an f-string
#------- can be placed inside quotes inside another f-string
print(f"I also said: '{y}'")

#--- Create a variable to hold a boolean value
hilarious = False
#--- Create a variable to hold a string which contains the
#------ ability to output another string inside it
joke_evaluation = "Isn't that joke so funny?! {}"

#--- Print a string that contains another variable string
print(joke_evaluation.format(hilarious))

#--- Create a variable holding a string
w = "This is the left side of..."
#--- Create a variable holding a string
e = "a string with a right side."

#--- Append two strings and print the result
print(w + e)
