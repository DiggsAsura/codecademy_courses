# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 10. OOP Pillar: Encapsulation

print("\n --- Introduction --- ")
print(" -------------------- \n")

# Encapsulation is the process of making methods and data hidden inside the object they 
# relate to. Languages accomplish this with what are called access modifiers like:
#
#   - Public
#   - Protected
#   - Private
#
# In general, public members can be accessed from anywhere, protected members can only be
# accessed from code within the same module and private members can only be accessed from
# within the class that these members are defined.
#
# Python doesn't have any inbuilt mechanism to prevent access from any member (i.e all
# members are public in Python). However, there is a common convention amongst developers
# to use a single underscore self._x to indicate that a member is protected. Accessing
# a protected member outside of the module will not cause an error, it is added by the
# developers to inform other developers that they should be careful when accessing this 
# member in such a manner.
#
# Similarly, we can declare a member as private with two leading underscores
# self.__x. This is more than just a convention in Python because of a mechanism called
# name mangling. Members that are preceded with two underscores have their names
# modified in the background to obj._Classname__x. While they can still be publicly 
# accessed, the purpose of this mechanism is to prevent clashing member names of any inheriting
# classes that might defina a member of the same name.
#
# Note that this is different from the dunder methods we discussed earlier. A dunder method
# has two leading and two trailing underscores and is treated differently than a 
# private member. One important difference is that dunder method names are not mangled.

# Ok so yea, wtf, lol. 
#

print("\n --- Tasks --- ")
print(" ------------- \n")

# 1. The Employee class contains one attribute id. An instance variable e is defined and then 
#    passed to the function dir() which is output to the console.
#
#    dir() is a built-in Python function that returns a list of all class members, including
#    dunder methods.
#
#    When you run the code, you will see a list of class members with id as the last element.
#
# 2. Now add an attribute that uses the single underscore naming convention.
#
#    Inside the Employee class .__init__() method:
#
#     - Define the single underscore variable _id and set it equal to whatever you want
#
#   When you run the code you can see _id as the second to last element in the 
#   output list.
#
# 3. Now define a variable using the double-underscore.
#
#    Inside the Employee class .__init__() method:
#
#     - Define the double underscore variable __id and set it equal to whatever you want
#
#    When you fun the code you can see a new variable _Employee__id as the first element 
#    in the output list. This is the result of name-mangling the variable self.__id

class Employee():
  def __init__(self):
    self.id = None
    self._id = 1
    self.__id = 1


e = Employee()
print(dir(e))

# Ok i see the namespace list is changing, but god knows what it's good for?!? 
