#---This import allows us to use module argv from package sys
import sys

#---This script exists to demonstrate use of '*args' 
def unknown_vars(args):

  print("This script exists to demonstrate use of '*args' as shown below.\n\n")
  print(f"This args list contains {len(sys.argv)} variables.")
  
#---I need a counter
  counter = 0
 
  #---List out all the variables
  for arg in args:
    print(f"Argument at index {counter} contains value {arg}")
    
    #---Apparently the ++ operator is not an operator in python
    counter+=1

#---If I define a function, it might behoove me to actually use it

unknown_vars(sys.argv)

