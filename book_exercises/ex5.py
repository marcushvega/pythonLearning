name = 'Zed A. Shaw'
age = 35       # not a lie
height = 74    # inches
weight = 180   # pounds
eyes = 'blue'
teeth = 'a bit more yellow than they are supposed to be'
hair = 'Brown'

cm_to_inches = 1 / 2.54
inches_to_cm = 2.54
lbs_to_kg_approx = 5 / 2.4
kg_to_lbs_approx = 2.4 / 5

print(f"Let's talk about {name}")

print(f"He's {height} inches tall")
print(f"That's {inches_to_cm * height} cm!")

print(f"He's {weight} pounds heavy")
print(f"That's {lbs_to_kg_approx * weight} kilograms!")
print(f"Actually that's not too heavy")

print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the meth")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
