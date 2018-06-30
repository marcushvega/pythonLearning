#--- Tell script to use class argv from module sys
from sys import argv

#--- Tell script to expect 2 arguments
script, filename = argv

#--- Use the open() method to open a File object
txt = open(filename)

#--- Print an f-string. F-string will use argument 2 as filename
print(f"Here's your file {filename}:")
#--- Output the contents of the filename specified in the command to run this script
print(txt.read())

#--- Close the read file
txt.close()
