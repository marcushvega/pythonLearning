#--- Allows script to use argv class from the sys module
from sys import argv
#--- read the WYSS section for how to run this
#--- Lets script know that it must expect 4 arguments from the command line
#------ where first argument must be the name of the script
script, first, second, third = argv

#--- Print name of script to command line
print("The script is called:", script)
#--- Print value of first variable to command line
print("The first variable is:", first)
#--- Print value of second variable to command line
print("The second variable is:", second)
#--- Print value of third variable to command line
print("The third variable is:", third)
