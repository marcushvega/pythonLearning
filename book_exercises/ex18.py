# this one is like your scripts with argv
#---a function named print_two gets defined
#------*args means you can use as many arguments (variables) as you want to
#------Only the '*' in '*args' is necessary. '*args' is just a convention
#------Example: '*vars' and '*args' would cause no change in the 
#---------functionality of the function
#------'*args' is effectively a list
def print_two(*args):
  #---Although you can use as many arguments as you want, this line specifies
  #------the number of arguments the script will expect to run. 
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")

# ok that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): 
  print(f"arg1: {arg1}, arg2: {arg2}")

# this one takes no arguments
def print_none():
  print("I got nothin'.")

# this one takes one argument
def print_one(arg1): 
  print(f"arg1: {arg1}")

# this takes as many arguments as you care to give it
def var_vars(*args)
  for arg in args:
    print(f"There are {len(*args) in this function"})

print_two("Zed", "Shaw", "third")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# an aside on '*args' can be found below
#---'*args' is used to send a --non-keyworded-- variable length 
#---argument LIST to the function.
#---Other singular arguments can be passed if you want the  
#---script to require a minimum of --> numVars > 0
#----->For an example, see script ../marcus_scripts/ex18_MV_args.py

#---There is another keyword that is similar to '*args'
#---This is keyword is '**kwargs'.
#---This keyword is similar in function, but the difference 
#------is this keyword allows for named variables to be 
#------inserted into the function.
#------>For an example, see script ../marcus_scripts/ex18_MV_kwargs.py
