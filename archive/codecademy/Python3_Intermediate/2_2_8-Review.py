# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Scope
# 8. Review

# Great job! You're learned some important concepts in Python regarding scope.
# In this lesson, we've covered:
#
# - The concept of scope and the LEGB rule
# - What the local scope is
# - What a nested function is and the enclosing/nonlocal scope
# - What the global scope is
# - How to modify behavior using the global statement
# - How to modify behavior using the nonlocal statement
#
# Knowing these concepts allows for a stronger mastery of Python when
# working with names in programs and taking into consideration what parts
# of the programs they can be accessed or modified.
#
# Keep up the great work!
#

def function1():
  global var1
  var1 = 1 # global namespace
  var2 = 2 # enclosing namespace
  
  def function2():
    nonlocal var2 # enclosing namespace
    global var3 # global namespace
    var2 += 1 # local namespace, hmm or not - enclosing?
    var3 = 3 # global namespace
    print(globals())
    print(locals())
  
  function2()
function1()
