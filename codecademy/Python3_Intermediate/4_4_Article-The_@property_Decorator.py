# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 4. Article
# The @property Decorator

# Introduction
print('''
The @property Decorator
Introduction - getters and setters recap
--------------------------------------------
''')
#
# In this article, we'll explore the @property decorator - a more pythonic way
# way to use getter and setters in our object-oriented programs! Before we
# dive in, let's briefly review the concept of getters and setters.
#
# Let's recall that getters and setters are useful tools for achieving
# encapsulation (a way to prevent data from direct modification). We can
# define a private attribute and then use getters and setters to expose a 
# public means of reading and modifying a class attribute value. Further,
# getters and setter moethods allows us to create complex behavior such
# as limiting access under certain conditions or imposing restrictions
# on allowable ranges of values for an atrribute. 
#
# Let's start by looking at an example class called Box with one attribute
# called weight. In this case, weight will be a private attribute with a 
# getter and a setter(getWeight() and setWeight()).

class Box:
  def __init__(self, weight):
    self.__weight = weight
    
  def getWeight(self):
    return self.__weight
  
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight
    
  def __repr__(self):
    return "Weight: {}".format(self.__weight)

b1 = Box(20)
print(b1)

# Notice two things:
#
#   - We want to follow best practices by denothing weight as a private attribute
#     using __ (dunder) notation. This, however, does not make an attribute 
#     private, and we can still manipulate them directly.
#
#   - We are also posing some restrictions on our setter so that the weight of
#     an instance of the Box class can only be set to values greater than zero.
#     We can see if this we try to manipulate an instance:

b2 = Box(10)
b2.setWeight(-5)
print(b2.getWeight()) # output 10

b2.setWeight(5)
print(b2.getWeight()) # output 5

# That our box weight was unchanged on the first call:
# 10
# 5
#
# Notice that we need to call the methods instead of directly interacting
# with the weight attribute. What if we could have the best of both worlds?
# That is, a way to directly interact with the weight attribute but still
# benefit from the complex behavior of methods such as the weight restriction.
# This is where the built-in function property() comes in.


print('''\n
Introduction
The built-in property() function
----------------------------------
''')
# The Python built-in property() function accepts four optional arguments:
# fget, fset, fdel and doc. The first three represents, getter, setter and
# deleter methods, respectively, and the last one is a docstring for the
# attribute. 
#
# Let's take a look at the advantages by refactoring our Box class:

class Box2:
  def __init__(self, weight):
    self.__weight = weight
    
  def getWeight(self):
    return self.__weight
  
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight
  
  def delWeight(self):
    del self.__weight
  
  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")
  
  def __repr__(self):
    return "Weight: {}".format(self.__weight)
  
# Notice we have added one additional method to our class called delWeight() to
# serve as a deleter for the property. While it is not strictly required, we will
# add it to show the full potential of the property() function. We then call
# the property() function and pass the getter, setter and deleter in as
# arguments. Theis will immediately allow us to use the follow syntax for 
# our class:

b3 = Box2(10)
print(b3.weight) # this calles .getWeight()
b3.weight = 5 # this called .setWeight()
del b3.weight # this calls .delWeight()
b3.weight = -5 # box.__weight is unchanged

# While this change, our program gains som eimmidiate benefits:
#
#   - We can now use the weight attribute as if it was public. We no 
#     longer have to call the setters, getters, and deleter methods directly 
#     and thus giving our program a simpler syntax.
#
#   - Even though we no longer call the methods directly, we still can
#     maintain constraints such as the weight limit in setWeight(). It's 
#     the best of both worlds!
#
#   - If we had a huge codebase that used our methods multiple times in 
#     multiple places, a single change to the method name would seriously 
#     mess up our program since we would have to change it everywhere!
#     We no longer have this issue using the property() method since
#     we never call it directly.
#
# While this is a bit advantage for our programs to be more "pythonic", we
# can go even further by using the decorator pattern to replace the need to 
# call the property() function altogether.


print('''\n
Introduction
@property Decorator
---------------------
''')

# The most pythonic way to define getters, setters and deleters is by using
# the @property decorator. This decorator is syntactic sugar for using the
# property() function and helps our code looks much cleaner. 
# Let's take a look:

class Box3:
  def __init__(self, weight):
    self.__weight = weight

  @property
  def weight(self):
    """Docstring for the 'weight' property"""
    return self.__weight
  
  @weight.setter
  def weight(self, weight):
    if weight >= 0:
      self.__weight = weight
  
  @weight.deleter
  def weight(self):
    del self.__weight
    
# Let's break this down:
#
#   - First, we have renamed all our methods to simply be weight()
#
#   - Then we denoted our getter with a @property. This marks the property
#     to be used as prefix for decorating the setter and deleter methods.
#
#   - Lastly, we use @weight.setter and @weight.deleter to define our
#     setter and deleter methods, respectively.
#
# This is the equivalent of doing:

#weight = property(getWeight, setWeight, delWeight, "docstring for...blabla")

# And thus giving us the same syntactical advantage as before:

b4 = Box3(10)
b4.weight = 5
del b4.weight

#
# Wrap up!
#
# To summarize, we learned:
#
#   - The limitations of using regular setter and getter methods.
#
#   - How to use the property() function to create cleaner getters, setters,
#     and deleters.
#
#   - The @property decorator is the most "pythonic" way to use the
#     property()