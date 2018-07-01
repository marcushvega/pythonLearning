#---This script exists to show use of '**kwargs'
#---Need method argv from sys module
import sys

def named_vars(**kwargs):
	print("The porpoise of this script is to demonstrate use of '**kwargs'.")
	
	print(f"This args list contains {len(kwargs)} items")

	#---Print values entered
	for name, value in kwargs.items():
		print('{0} = {1}'.format(name, value))
	
named_vars(first_arg=1, second_arg=2, third_arg='seventeen')

