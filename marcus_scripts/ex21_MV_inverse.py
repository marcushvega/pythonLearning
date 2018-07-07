# Write a simple formula and use the functions in the same way to calculate it
#---Apparently I will be using the same functions as are in ex21.py in book_exercises folder
##---I suppose it is necessary to say this will download an image. If you don't want to download an image, you should press CTRL + C when prompted.
##---Info on line 3 does not matter as those lines have been commented out.

#---Need requests module to check my answer against internet answer
import requests

#---Necessary for my final conclusion
#import urllib.request
#from PIL import Image

def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b

#---> 12 + 98 - 32 + 1015 / 9 * 17 <---

print("Outputting answer to: 12 + 98 - 32 + 1015 / 9 * 17")

#---Attempt to use PEMDAS to calculate answer
answer=subtract(add(12, 98), add(32, (divide(1015, multiply(9, 17)))))

print(f"Script Answer: {answer}")

print("Checking internet answer using math.js webservice.")

#---Use math.js webservice to check my work
r = requests.get('http://api.mathjs.org/v4/?expr=12%2B98-32%2B1015%2F9*17')

print(f"Math.js webservice answer: {r.text}")

#---Set certain variables based on whether answers are equal to each other
if (float(r.text) == answer):
	equal = 'are'
	marcus = 'Looks like I did something correctly.'
else:
	equal = 'are not'
	marcus = 'Looks like I need to rewrite my equation.'

#---Send some text to the screen
print(f"It appears that the math.js webservice answer of {r.text} and the python script answer of {answer} {equal} equal to each other")

#---Send some more text to the screen
print(marcus)

#---My PEMDAS answer appeared to be incorrect...or the webservice's answer is incorrect
#---Rewrite equation using functions without regard to PEMDAS
new_answer = add(12, subtract(98, add(32, (divide(1015, multiply(9, 17))))))

print(f"My new answer, without regard to PEMDAS is {new_answer}")

#---I got a bit off-track the original idea of this exercise
#print("\n\nPress 'C' to see my conclusion. Press CTRL + C if you do not want to see my conclusion.")
#some_input = input()
#/
#if some_input != 'C':
#	print(f"But some other key such as {some_input} is fine, too")
#
##---Download necessary conclusion image
#urllib.request.urlretrieve("m.memegen.com/peet8x.jpg", "ex21_conclusion.jpg")
#
#---Open necessary conclusion image
#img = Image.open('ex21_conclusion.jpg')
#img.show()


