# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 1. Namespaces
# 4. Enclosing Namespace

#global_variable = 'global'

#def outer_function():
#  outher_value = 'outer'
  
#  def inner_function():
#    inner_value = 'inner'

#  inner_function()
#  print(locals())

#outer_function()

# Note:
# - We define a function called outer_function() and nest another function
#   inside it called inner_function(). To generate a namespace, functions 
#   must be executed, so we are calling both of them.
#
# - Here, the outer_function() serves the role of an enclosing function while
#   inner_function is an enclosed function. By createing this structure, 
#   we generate an enclosing namespace - a namespace created by an enclosing
#   function and any number of enclosed functions inside it.

# While Python doesn't give us any particular function like enclosing() to
# visualize the namespace, we can use locals() to see when enclosed
# namespaces are generated. Let's take a look by modifying our script (did above)

# Notice the 'inner_function': <function outer_function.<locales>.inner_function
# shows that our local namespace inside of outer_function() encloses the local
# namespace of inner_function()

# Uh, ok. xD

global_variable = 'global'

def outer_function():
  outer_value = "outer"
  
  def inner_function():
    
    def inner_nested_function():
      nested_value = 'nested'
    inner_nested_function()
    print(locals())
  
  inner_function()
  #print(locals())
outer_function()

