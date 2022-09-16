# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Scope
# 7. Scope Resolution: The LEGB Rule

# While most of our focus so far has been around where we can access 
# namespaces, to truly get a full picture of scoping rules, we must also
# examine how Python handles scope resolution.
#
# Scope resolution is a term used to describe a search procedure for a 
# name in the various namespaces. A set of rules dictates the order
# that the search needs to follow.
#
# In Python, the unofficial rule (often referred to in literature but does 
# not exist in the official documentation) is known as the LEGB rule.
#
# LEGB stands for Local, Enclosing, Global and Built-in. These four
# letters represent the order of namespaces Python will check to see if an 
# name exists. Here is a visualization of the order:
#
#   1. Built-in Scope
#          ^
#   2. Global Scope
#          ^
#   3. Enclosing Scope
#          ^
#   4. Local Scope
#
# To see this rule in action, let's take a look at the two specific scenarios
# where Python is searching for a name. The first scenario is a nested function
# that wants to print a variable called age:
#
#age = 27
#def func():
#  def inner_func():
#    print(age)
#  inner_func()
#func()
#
# Output:
# 27
#
# So what exactly happend here in terms of scope resolution? It went a bit 
# like this:
#
# 1. First, Python looked in the local (The L of LEGB) scope that existed 
#    inside of inner_func(). This is the lowest level of LEGB rule and 
#    thus where Python starts to search for a name that is trying to be called
#    (in this case via print()). Python then realized the name of age isn't
#    in the local namespace and continues the search to the upper levels
#    of scope.
#
# 2. The second level Python examined is the enclosing scope (The E of LEGB)
#    of func(). Unfortunately, again the name of age doesn't exist in the
#    enclosing namespace, and Python moves upwards to higher scopes.
#
# 3. Next, Python arrives at the global scope and finds the name of age in
#    the global namespace. The serach is finished, and the result is returned.
#
# This process of scope resolution is cruicial to understanding how programs
# are able to access names in different scopes. Keep in mind the order that 
# Python searches always start at the lowest level (the local level) and
# always flows upwards to the higher scopes. 
#
# The second scenario to examine is seeing what happens when we have two
# of the same name in different namespaces.
#
# Let's examine the same script but with a slight modification that creates
# a second name called age in a different namespace. Here is what it 
# looks like:
#
#age = 27
#def func():
#  age = 42
#  def inner_func():
#    print(age)
#  inner_func()
#func()
#
# Output:
# 42
#
# Here the output will be 42 because Python could find a name (age) in the
# enclosing scope and did not continue to search for the value up into the
# global scope. If Python cannot find a name in any of the four scopes it
# searches, it will return a NameError exception.


color = 'green'

def change_color(new_color):
  global color
  to_update = new_color
  
  def disp_color():
    print("The original color was " + color)
  disp_color()
  
  color = to_update
  print("The new color is: " + color)
  
change_color("blue")