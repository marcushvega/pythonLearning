#---Method is defined
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#---print text to terminal, use vars in some text
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

#---Print text to terminal
print("We can just give the function numbers directly:")
#---Call cheese_and_crackers method
cheese_and_crackers(20, 30)

#---Print text to terminal
print("OR, we can use variables from our script:")
#---Define and set variable to 10
amount_of_cheese = 10
#---Define and set another variable to 50
amount_of_crackers = 50

#---Call cheese_and_crackers method
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#---Print text to terminal
print("We can even do math inside too:")
#---Call cheese_and_crackers method using math within params
cheese_and_crackers(10 + 20, 5 + 6)

#---Print text to terminal
print("And we can combine the two, variables and math:")
#---Call cheese_and_crackers method using variables and math
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
