#---import module argv from package sys
from sys import argv

#---tell script to expect 2 parameters
script, input_file = argv

#---define method to take one parameter to specify a file
def print_all(f):
	#---read the specified file
	print(f.read())

#---define method to take one parameter to specify a file
def rewind(f):
	#---move cursor to beginning of file
	f.seek(0)

#---define method to take two (2) parameters;
#------first param specifies which line to read
#------second param tells from which file line should be read
def print_a_line(line_count, f):
	#---print to terminal the text on line number {line_count}
	print(line_count, f.readline())

#---open the file specified in terminal as second parameter
current_file = open(input_file)

#---print stuff to terminal
print("First let's print the whole file:\n")

#---print the entire contents of the current_file, specified in terminal as second parameter
print_all(current_file)


#---print stuff to terminal
print("Now let's rewind, kind of like a tape.")

#---move cursor back to beginning of file
rewind(current_file)

#---print stuff to terminal
print("Let's print three lines:")

#---set current line to line 1 in file
current_line = 1
#---print to terminal the contents of the first line in file
print_a_line(current_line, current_file)

#---set current line to previous line number plus one (1) ==> (2)
current_line = current_line + 1
#---print to terminal the contents of line 2 (1 + 1)
print_a_line(current_line, current_file)

#---set current_line to previous line number plus one (1) ==> (3)
current_line = current_line + 1
#---print to terminal the ccntents of line 3 (2 + 1)
print_a_line(current_line, current_file)

