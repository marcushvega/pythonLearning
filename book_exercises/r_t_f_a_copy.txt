from sys import argv

script, filename = argv

#--- Open file filename
txt = open(filename, 'r')

#--- Output contents of file filename to the screen
print(txt.read())

#--- Close file filename
txt.close()
