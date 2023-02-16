# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Scope
# 4. Modifying Scope Behaviour: nonlocal Statement

# We just witnessed that we can access names from the enclosing scope
# with nested functions, but we cannot modify them. Python does however
# provide a way for us to modify names in the enclosing scope, by using
# the nonlocal statement.
#
# Given the following enclosing and nested function, there is a variable
# defined in the enclosing scope, which is not modifiable from within
# the nested function.
#
#def enclosing_function():
#  var = "value"
#  def nested_function():
#    var = "new_value"
#  nested_function()
#  print(var)
#enclosing_function()
# 
# This will output:
# value
#
# as the value of var was not modified by the nested function. After using
# the nonlocal statement, the variable is now modifiable from the local 
# scope.
#
#def enclosing_function():
#  var = "value"
#  def nested_function():
#    nonlocal var
#    var = "new_value"
#  nested_function()
#  print(var)
#enclosing_function()
# This will output:
# new_value
#
# Allright - this is probably one to remember.

walls = [(20, 9), (25, 9), (20, 9), (25, 9)]

def calc_paint_amount(wall_measurements):
  
  square_feet = 0
  
  def calc_square_feet():
    nonlocal square_feet
    
    for width, height in wall_measurements:
      square_feet += width * height
      
  def calc_gallons():
    return square_feet / 400
  
  calc_square_feet()
  return calc_gallons()

print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))