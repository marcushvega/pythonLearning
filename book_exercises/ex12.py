#--- Prompt the user for his or her age
age = input("How many years old are you? ")
#--- Prompt the user for his or her height
height = input("How tall are you? ")
#--- Prompt the user for his or her weight
weight = input("How much do you weigh? ")
#--- Prompt the user for unit of weight from last question
unit_of_weight = input("In which units is your answer for weight (kg, lbs, stone, etc.,) ? ")

#--- Print stuff
print(f"So, you're {age} years old, {height} tall, and {weight} {unit_of_weight} heavy.")
