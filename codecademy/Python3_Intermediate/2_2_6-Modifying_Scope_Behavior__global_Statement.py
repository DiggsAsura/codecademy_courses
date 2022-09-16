# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Scope
# 6. Modifying Scope Behaviour: global Statement

# Sometimes, we want to modify a global name from within a local scope. How
# do we go about doing this?
#global_var = 10
#def some_function():
#  global_var = 20
#some_function()
#print(global_var)
# 
# The output would be:
# 10
#
# In the above example, the value of global_var remains 10 because 
# global_var = 20 is in a local scope.
#
# Similar to the nonlocal statement, Python provides the global statement
# to allow the modification of global names from a local scope
#global_var = 10
#def some_function():
#  global global_var 
#  global_var = 20
#some_function()
#print(global_var)
#
# Output:
# 20
#
# In addition, the global statement can be used even if the name has not 
# been defined in the global namespace. Using the global statement would
# create the new variable in the global namespace.
#def some_function():
#  global kenneth
#  kenneth = 37
#some_function()
#print(kenneth)
# 
# Output:
# 37
#
# In summary, the global keyword is used within a local scope to associate
# a variable name with a name in the global namespace. This association is
# only valid within the local scope global is used.

def print_available(color):
  global paint_gallons_available
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons of available of ' + color + ' paint.')
  
print_available('red')
for color in paint_gallons_available:
  print(color)