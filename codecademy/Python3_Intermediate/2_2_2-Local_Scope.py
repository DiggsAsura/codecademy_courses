# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Scope
# 2. Local Scope

#def favorite_color():
#  color = "Red"
#print(color)

# Whenever we decide to call a function, a new local scope will be generated.
# Each subsequent function call will generate a new local scope. Since the
# local scope is the deepest level of the four scopes, names ina local scope 
# cannot be accessed or modified by any code called in outer scopes. As
# a rule of thumb, any names created in a local namespace are usually
# also locally scoped.
#
# In this case, the name of color is scoped locally to the function
# favorite_color(). Since the staement print(color) is called outside of the
# function, it has no access to the local scope (and thus the local 
# namespace) inside of favorite_color() and returns an error.
#
# However, if we were to refactor our code.
#def favorite_color():
#  color = "Red"
#  print(color)
#favorite_color()
#
# Then, we wouldn't have trouble accessing the name of color since now the 
# print() function is cooped locally, and our output would return 'Red'.
#
# Let's take some time to practice the basics of local scope!

def painting(paint_colors, picture):
  painting_statement = "To paint the " + picture + " we need the following colors: "
  print(painting_statement)
  for color in paint_colors:
    print(color)
    
painting(['Blue', 'Yellow'], 'Ukraine')