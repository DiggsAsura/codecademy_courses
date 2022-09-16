# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Global Namespace

# The global namespace exists one level below the built-in namespace.

#import random
#first_name = "Jaya"
#last_name = "Bodegard"

#def print_variables():
#  random_number = random.randint(0,9)
#  print(first_name)
#  print(last_name)
#  print(random_number)

#print_variables()
#print(globals()) # globals() is ironically a built-in namespace though

# Will print out globals. This shows us a lot of "nonsense" stuff, but 
# important to know it contains all of the non-nested objects of our program.
# This includes the variables first_name and last_name as well as the function
# print_variables(). 
#
# However does not include random_number because it is nested inside of our 
# function - which we will learn more about in the next exercise. 
#
# Also, anytime we use the import statement to bring a new module into 
# our program, instead of adding every name from that module (such 
# as all the names in the random module) to our current global namespace, 
# Python will create a new namespace for it. This means there might be 
# potentially multiple global namespaces in a single program. This will 
# be masked away from us in the format seen with the random module
# (<module 'random' from '/us/lib/python3.9/random.py).

print(' -- Globals Namespace with empty script -- \n')
print(globals())

global_variable = 'global'

def print_global():
  global_variable = 'nested global'
  nested_variable = 'nested value'


print('\n -- Globals Namespace non-empty script -- \n')
print(globals())

# Takeaways:
#   - As we saw previously, the global namespace only contains items that
#     non-nested. In this case, our global namespace does not contain the
#     identical nested name of global_variable
#
#   - Depending on where we call globals() we will have a different 
#     namespace generated. this means globals() will sho the namespace
#     at the time it was executed. Since we called globals() a second time 
#     after defining a few items (such as variables and functions), those
#     items now show up in the global namespace. 