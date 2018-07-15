import sys
#---Apparently importing specific module isnt necessary?
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
	line = language_file.readline()

	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)


###---Unknown symbols from this exercise---###
# line.strip()
# STRING.encode(encoding, errors)
# STRING.decode(encoding, errors) --> can only strings that have been encoded be decoded?
# ---> example in method print_line where next_lang is encoded and that encoded variable then gets decoded
# Defining a main method is also new

# Why does this script not require some kind of loop? <--- nvm. recursion in main(x, y, z) method

# encode - encoding is an agreed-upon standard for how sequences of bits should represent a number
# ---> today we call a byte a sequence of 8 bits
# ---> once we have bytes, we can store and display text after deciding on another convention
# ------>to how a number should represent a letter
# ASCII is the most popular convention. 
# ---> ASCII maps a number to a letter.
# ---> ASCII - Americant Standard Code for Information Interchange
# ---> With the ASCII Convention, we can "STRING" characters together to form a word
# ---> ASCII uses 8 bits to map a number to a letter
# ---> ASCII fails in that it can only encode a maximum of 256 characters, 
# ------> but there are far more than 256 characters in all the world's langugages

# Unicode is another encoding convention.
# ---> Unicode was created to be a "universal encoding" of all human languages.
# ---> Unicode uses 32 bits to map a number to a letter
# ---> Unicode can encode a maximum of 2^32 = 4,294,967,295 characters
# ------> 4 billion characters can hold every current human language and has extra space for more characters

#######################################
######------> End Tomato <------#######
#######################################


