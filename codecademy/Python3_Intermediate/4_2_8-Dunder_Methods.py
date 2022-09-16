# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 8. Dunder Methods

from tkinter import E


print("\n --- Introduction ---")
print(" -------------------- \n")
#
# The code below shows that when working with different object typs like, int,
# str or list, the + operator performs different functions. This is known
# as operator overloading and is another form of polymorphism.

# For an int and an int, + returns an int
2 + 4 == 6

# For a string and a string, + returns a string
"Is this " + "addidtion?" == "Is this addition?"

# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]

# To implement this behavior, we must first discuss dunder methods. Every
# defined class in Python has access to a group of these special methods.
# We've explored a few already, the constructor __init__() and the string 
# representation method __repr__(). The name dunder method is derived from 
# the Double UNDERscores that surround the name of each method.
#
# Recall that the __repr__() method takes only one parameter, self, and must
# return a string value. The returned value should be a string representation
# of the class, which can be seen by pusing print() on an instance of 
# the class. Review the sample code below for an example of how this method 
# is used.
#
# Defining a class's dunder methods is a way to perform operator overloading.

class Animal:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

  def __add__(self, another_animal):
    return Animal(self.name + another_animal.name)
  
a1 = Animal("Horse")
a2 = Animal("Penguin")
a3 = a1 + a2
print(a1)
print(a2)
print(a3)

# Output:
# Horse
# Penguin
# HorsePenguin

# The above code has the class Animal with a dunder method, .__add__(). This
# defines the + operator behavior when used on objects of this class type. The
# method returns a new Animal object with the names of the operand objects
# concatenated. In this example, we have created a "HorsePenguin"!
#
# The line of code a3 = a1 + a2 invokes the .__add__() method of the left
# operand, a1, with the right operand a2 passed as an argument. The name
# attributes of a1 and a2 are concatenated using the .__add__() parameters,
# self and another_animal.
# The resulting string is used as the name of a new Animal object which is
# returned to become the value of a3.


print("\n --- Tasks --- ")
print(" ------------- \n")
#
# 1. There is now a Meeting class with an attendees list attribute and 
#    an .__add__() dunder method that add Employee intances to the attendees
#    list. Before we try and add employees to a meeting, we want to make sure
#    we can know how many employees are in a meeting.
#
#    Inside the Meeting class:
#     - Overload the len() operation by defining a __len__() dunder method
#
#     - Inside the __len__() definition, return the length of the attribute
#       attendees
#
# 2. Now add three employees to a meeting:
#
#     - Using the Meeting instance m1, add each of the employee instances e1,
#       e2, and e3. Use one line for each employee instance.
#
#     - Ourput the length of meeting instance m1
#
#    You should see the output from each employee being added and then the 
#    length of the meeting, 3. 

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
  
class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)
  
  def __len__(self):
    return len(self.attendees)

e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()

att = [e1, e2, e3]
for e in att:
  m1 + e

print(len(m1))