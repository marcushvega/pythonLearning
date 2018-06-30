# In this exercise, we make a simple little text editor

#--- Tell script to use module argv from package sys
from sys import argv

#--- Tell script to expect 2 arguments
script, filename = argv

#--- Print the second argument
print(f"We're going to erase {filename}.")
#--- Give user instructions
print("If you don't want that, hit CTRL-C (^C).")
#--- Give user more instructions
print("If you want that, hit RETURN.")

#--- Allow for user input
input("?")

#--- Print text to screen
print("Opening the file...")
#--- Open file specified by specified by second argument for writing
target = open(filename, 'w')

#--- The lines between the hashes are redundant because the open method 
#------ used with the write option truncates the file anyway
###############################################
print("Truncating the file. Goodbye!")
#--- Truncate all contents in the file
target.truncate()
###############################################

#--- Print text on the screen
print("Now I'm going to ask you for three lines.")

#--- Prompt user for input
line1 = input("Line 1: ")
#--- Prompt user for input
line2 = input("Line 2: ")
#--- Prompt user for input
line3 = input("Line 3: ")

#--- Print text to the screen
print("I'm going to write these to the file.")

#--- Put the three new variables into an array for later laziness
lineArray = [line1, line2, line3]

#--- Output to the file each line on its own...line
for val in lineArray: 
  target.write(val)
  target.write("\n")

#--- Output text to the screen
print("And finally, we close it.")
#--- Close the file
target.close()
