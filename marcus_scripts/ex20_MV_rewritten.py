#---removed all comments I deemed unnecessary
from sys import argv

script, input_file = argv

#---print entire contents of specified file
def print_all(f):
	print(f.read())

#---move cursor back to beginning of file
def rewind(f):
	f.seek(0)

#---print to the terminal text from line number {line_count} from file {f}
def print_a_line(line_count, f):
	print(line_count, f.readline())

#---open the file specified as second parameter when running script from command line
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#---move cursor back to beginning of file
rewind(current_file)

print("Let's print three lines:")

#---print out first 3 lines in file
current_line = 0
while current_line < 3:
	current_line += 1
	print_a_line(current_line, current_file)

#-The porpoise of this exercise was to learn to use the += operator
#-The below lines are from the original exercise

#---set current line to line 1 in file
#current_line = 1
#print_a_line(current_line, current_file)

#---set current line to previous line number plus one (1) ==> (2)
#current_line = current_line + 1
#---print to terminal the contents of line 2 (1 + 1)
#print_a_line(current_line, current_file)

#---set current_line to previous line number plus one (1) ==> (3)
#current_line = current_line + 1
#---print to terminal the ccntents of line 3 (2 + 1)
#print_a_line(current_line, current_file)

