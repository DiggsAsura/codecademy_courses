# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Scope
# 3. Enclosing/Nonlocal Scope

# Similar to how nested functions form a unique namespace within their 
# enclosing functions (the enclosing namespace), there also exist special
# rules that apply for accessing nested values. These rules make up the 
# enclosing scope (also known as nonlocal scope). Let's take a look at a 
# nested function to see the scope in action:

#def outer_function():
#  enclosing_value = 'Enclosing Value'
  
#  def nested_function():
#    nested_value = 'Nested Value'
#    print(enclosing_value)
  
#  nested_function()
  
#outer_function()
#
# Our output: 
# Enclosing Value
#
# Enclosing scope allows any value defined in an enclosing funtion to be 
# accessed in nested functions below it. We can observe this scope since
# nested_function() can acacess a variable defined one level above in the 
# enclosing function (outer_function()).
#
# We can also observe this scoping rule further if we nested a function one 
# level deeper:

#def outer_function():
#  enclosing_value = 'Enclosing Value'
#  def nested_function():
#    nested_value = 'Nested Value'
#    def second_nested():
#      print(enclosing_value)
#      print(nested_value)
#    second_nested()
#  nested_function()
#outer_function()
#
# Would output:
# Enclosing Value
# Nested Value
#
# There are two caveats to be aware of with enclosing scope:
#
# - The flow of scope access only flows upwards. This means that the deepest
#   level has access to every enclosing namespace above it, but not the 
#   other way around. For example, if we tried to access nested_value from
#   one level above where it was defined, the program would produce an 
#   error: 
#   NameError: name
#   'nested_value' is not defined
#
# - Immutable objects, such as string or numbers, can be accessed in nested
#   functions, but cannot be modified. Let's try to change enclosing_value
#   to see this restriction in action
#
#def outer_function():
#  enclosing_value = 'Enclosing Value'
#  def nested_function():
#    enclosing_value += 'changed'
#  nested_function()
#  print(enclosing_value)
#outer_function()
#
#   would output:
#   UnboundLocalError: local variable 'enclosing_value' referenced before
#   assignment
#
# Let's now practice accessing values in the enclosing scope!

def calc_paint_amount(width, height):
  square_feet = width * height
  def calc_gallons():
    return square_feet / 400
  return calc_gallons()
  
print('Number of paint gallons needed. ')
print(str(calc_paint_amount(30,20)))