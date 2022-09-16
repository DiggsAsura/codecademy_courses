# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 2. Scope
# 1. Local Scope

# Recall, in Python, namespaces are the backbone of how our programs are
# stored and retrieved. However, knowing about namespace mechanism isn't
# enough to explain the following behaviour:
#def printColor():
#  color = 'red'
#print(color)
#
# If we run this code, our output would be:
# NameError: name 'color' is not defined
#
# Well, that's puzzling. We can see that there clearly exists a name 
# called color, and we know anytime we define a variable it gets added to a 
# namespace, yet we can't seem to access it! What gives?
#
# Well, this is where a concept called scope come into play. Scope defines 
# which namespaces our program will look into (to check names) and in 
# what order. While multiple namespaces usually exist at once, this does
# not mean we can access all of them in different parts of our program!
# Exploring the concept of scope will allow us to start recognizing
# when and where certain objects may or may not be accessed.
#
# Similar to namespaces, there are four different levels of scope.
# These levels are:
# 1. Built-in Scope (We will skip talking about this scope)
# 2. Global Scope
# 3. Enclosing Scope
# 4. Local Scope
#
# Those four scope names should look very familiar since those are also the
# four namespaces we talked about! Each of these scopes has a different
# level of access to the namespaces our programs generate. In the next few
# exercises, we will examine each of these scopes.
#
# Note: As we explore the ideas around scope, there may be some confusion
# between what distinguishes the concept of scope and namespaces. While 
# both concepts are interlinked and work together, namespaces are simply
# the mechanism for storing name-object pairs (dictionary), while scope will
# serve as a rule system on where (which point in our code) we can retrieve
# those names. 

print("""
      Scope hierarchy:
      
      Built-in Scope
      
      Global Scope
      
      Enclosing Scope
      
      Local Scope
      
      """)
