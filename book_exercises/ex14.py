#--- Tells the script to use class argv from the sys module
from sys import argv

#--- Tells the script to expect 2 arguments
script, user_name = argv
#--- Creates a variable to hold character sequence '> '
prompt = '> '

#--- Prints strings and variables to the screen
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
#--- Prompts user for input
likes = input(prompt)

print(f"Where do you live {user_name}?" )
#--- Prompts user for input
lives = input(prompt)

print("What kind of computer do you have?")
#--- Prompts user for input
computer = input(prompt)

#--- Checks user input
if computer.lower() != "mac" or computer.lower() != "pc" or computer.lower() != "none":
#--- If invalid input is entered, the flag sets to False
  valid_word = False
else:
#--- If valid input is entered, the flag sets to True
  valid_word = True

#--- Continuously prompts for input and then tests for valid input until valid input is entered
while valid_word is False:

  print("""
  Please enter which kind of computer you have from the following list:
  \t* PC
  \t* MAC
  \t* NONE
  """)

  computer = input(prompt)

#--- Sets valid_word to True if a valid word is entered
  if computer.lower() == "mac" or computer.lower() == "pc" or computer.lower() == "none":
#--- Setting of variable will cause loop to exit
      valid_word = True

#--- Last line to print changes if computer == "none"
if computer.lower() == "none":
  has_computer = "You poor (unfortunate) poor (lacking wealth) human (self-explanatory)."
elif computer.lower() == "pc":
  has_computer = "How's that working out for you?"
else:
  has_computer = "Ah, have they finally gotten rid of that nasty microphone hole?"

#--- Prints values based on values entered during runtime of script
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
I see you have a {computer}. {has_computer}
""")
