# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Function Arguments
# 2. Variable number of arguments: *args

# To start explorint variable argument lenghts in Python functions, let's
# take a look at a familiar function we have been using for a long time:
#print('This', 'is', 'the', 'print', 'function')
#
# Notice how the print() function does not care how many arguments we pass to it.
# It has no expectation that we are going to pass in one argument or even a 
# million! So the question is, how does print() accomplish this?
#
# Well, in Python, there is an additional operator called the unpacking
# operator (*). The unpacking operator allows us to give our functions a 
# variable number of arguments by performing what's known as
# "positional argument packing".
#
# Let's explore how it works by examining a basic function that utilizes
# the unpacking operator:
#def my_function(*args):
#  print(args)
#
# If we called this function with random arguments:
#my_function('Arg1', 245, False, True)
# 
# Our output would show us what is inside of *args:
#('Arg1', 245, False, True)
#
# Notice two things:
#
#   - In our print() call, we simply use the name of args with the unpacking
#     operator omitted. The name of args is completely arbitary, and this example
#     works just the same
#def myfunction2(*randomname):
#  print(randomname)
#
#   - Whatever name follows the unpacking operator (*) will store the arguments passed
#     into the function in the form of a tuple. This allows our functions to accept 
#     any number of arguments just like the print() function we examined earlier. In
#     this case, args has three values inside, but it can have many more (of fewer).
#
# Let's practice using the unpacking operator for positional arguments in a 
# function!

# Tasks
# 1. Jiho wants to expand our resturant application to also take orders from customers.
#    This is the perfect time to use the unpacking operator since we never know how
#    how many items customers are going to order. 
#   
#    To start, we want to build a function that will compile a list of all the items a 
#    customer wants to order and then print it out. This will help our kitchen to 
#    know what to cook.
#
#    Define a function called print_order() that will take in a variable number of 
#    arguments using a parameter called order_items. The function should
#    simply print order_items
#
# 2. Looks like... ups forgot to write the rest. Does it matter? I basically only 
#    write it all down to try memorise better. 

def print_order(*order_items):
  print(order_items)

order_1 = print_order("Orange Juice", "Apple Juice", "Scrambled Eggs", "Pancakes")
print(order_1)

print_order("Orange Juice", "Beer", "Coffee", "Hamburger")

# Interesting - if making a variable out of it first (order_1), output will add a None.
# This is not explained now but maybe later? 
