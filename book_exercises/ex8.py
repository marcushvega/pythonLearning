#--- Create an f-string with the ability to take in 4 more strings
formatter = "{} {} {} {}"

#--- Enter one number into each pair of braces
print(formatter.format(1, 2, 3, 4))
#--- Enter one string into each pair of braces 
print(formatter.format("one", "two", "three", "four"))
#--- Enter one boolean value into each pair of braces
#------ '+' will OR the boolean values together (False = 0, True = 1) 
#------ '*' will AND the boolean values together (False = 0, True = 1)
#------ ' ' will break the code
print(formatter.format(True+False, False*False, True*True, True+True))
#--- Enter the formatter variable into each pair of braces
print(formatter.format(formatter, formatter, formatter, formatter))
#--- Enter one String into each pair of braces; Use multiple lines for easier reading
print(formatter.format(
   "Try your",
   "Own text here",
   "Maybe a poem",
   "Or a song about fear"
))
