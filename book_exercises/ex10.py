tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."
backspace_cat = "\tI'm tabbed in.\n\t\bI'm tabbed but backspaced in.\n\t\b\b\bTabbed + 3 backspaces"
formfeed_cat = "This is a \f formfeed?"
linefeed_cat = "The linefeed character is the newline character in other languages"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

skinny_cat = '''
Here is another list (formfeed):\f*Eat\f*My\f*Shorts
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)

print(backspace_cat)
print(formfeed_cat)
print(linefeed_cat)

print(fat_cat)
print(skinny_cat)
