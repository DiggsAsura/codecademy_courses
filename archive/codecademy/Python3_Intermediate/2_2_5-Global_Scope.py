# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Scope
# 5. Global Scope

# At the highest level of access, we have the global scope. Names defined
# in the global namespace will automatically be globally scoped and can
# be accessed anywhere in our program. 
#
# For example:
#gravity = 9.8
#def get_force(mass):
#  return mass * gravity
#print(get_force(60))
# Would output
# 588.0
#
# However, similar to local scope, values can only be accessed but not
# modified. For example, if we tried to manipulate the value of gravity:
#gravity = 9.8
#def get_force(mass):
#  gravity += 100
#  return mass * gravity
#print(get_force(60))
# Would output
# UnboundLocalError: local variable 'gravity' referenced before assignment
#
# We probably shouldn't be manipulating gravity anyway! Let's practice 
# accessing values in the global scope to get a hang of it.

#def print_available(color):
paint_gallons_available = {
  'red': 50,
  'blue': 72,
  'green': 99,
  'yellow': 33
}
def print_available(color):
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


def print_all_colors_available():
  for color in paint_gallons_available:
    print(color)

print_available('red')
print_all_colors_available()