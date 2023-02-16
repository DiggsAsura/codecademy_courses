# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 1. Namespaces
# 5. Review

# Great job! You've learned some important concepts in Python regarding
# namespaces.
# 
# In this lesson, we've covered:
#
# - Names as identifiers for objects in Python.
#
# - What namespaces are.
#
# - The built-in namespace and how to access it using __builtins__.
#
# - The global namespace and how to acces it using globals()
#
# - The local namespace and how to access it using locals()
#
# - The enclosing namespace - a special type of local namespace that
#   occus when working with nested functions.
#
# Knowing these concepts allows for a stronger mastery of Python since names
# are the basis of how our programs store and retrieve information. Keep up
# the great work!

# Namespace tree:

# BUILT-IN NAMESPACE
# GLOBAL NAMESPACE
# LOCAL / ENCLOSING NAMESPACE

print("""
      Buil-in Namespace
      
      Global Namespace
      
      Local / Enclosing Namespace
      
      """)

print("\n BUILT-INS\n")
print(dir(__builtins__))

print("\n GLOBALS\n")
print(globals())

print("\n Locals / Enclosing \n")
def local_stuff():
  some_stuff = "ok"
  print(locals())
local_stuff()