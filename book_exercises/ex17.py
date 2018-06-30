#--- Import module argv from package sys
from sys import argv
#--- Import module exists from package os.path
from os.path import exists

#--- Let script know to expect 3 parameters
script, from_file, to_file = argv

#--- Output text to screen
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
###in_file = open(from_file)
###indata = in_file.read()
#--- Open, read, and then close file referenced in object from_file
indata = open(from_file).read()

#--- Output number of bytes in length the input file is
###print(f"The input file is {len(indata)} bytes long.")

#--- Display text showing user whether specified output file already exists
###print(f"Does the output file exist? {exists(to_file)}")
###print("Ready, hit RETURN to continue, CTRL-C to abort.")
###input()

#--- open file referenced by to_file in 'write' mode 
out_file = open(to_file, 'w')
#--- write data kept in variable indata to file referenced in out_file object
out_file.write(indata)

#--- Display message on screen
print("Alright, done.")

#--- Close file referenced by out_file
out_file.close()

#--- in_file not necessary when file is opened and read in one statement
###in_file.close()
