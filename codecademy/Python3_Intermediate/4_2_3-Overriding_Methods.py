# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 3. Overriding Methods

# When implementing inheritance, a child class may want to change the behavior
# of a method from its parent class. In Python, all we have to do is override
# a method definition. An overridden method in a subclass is one that has the
# same definition as the parent class but contains different behavior.

from curses.ascii import EM


print("\n --- Example(s) --- \n")

class Animal:
  def __init__(self, name):
    self.name = name
    
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))

pet1 = Animal("Rex")
pet1.make_noise()

# Output:
# Rex says, Grrrr

# The animal class above has one attribute, self.name and one method, 
# .make_noise(). The .make_noise() method outputs a somewhat generic animal
# sound, "Rex says, Grrrr". If we define a subclass of Animal we may want
# to make a different sound.

class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))

pet2 = Cat("Maisy")
pet2.make_noise() 

# Output
# Maisy says, Meow!

# Now we've made a class for a more specific type of animal, Cat. It has all the 
# attributes and methods of Animal. However, if you call the .make_noise() 
# method on this instance of Cat it will say "Maisy says, Meow!".


print("\n\n --- Tasks --- \n")
# ===============================

# 1. As an admin, you feel it is not important to give your ID, but just let
#    others know they're talking to an admin. 
#
#    Inside the Admin class:
#     - Define a method say_id()
#     - Inside the method, output "I am an Admin"
#
#    Now when you call .say_id() with e3 you should see the .say_id() method
#    output from Admin

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
    
  def say_id(self):
    print("My id is {}.".format(self.id))
    
class Admin(Employee):
  def say_id(self):
    print("I am an Admin.")
  
e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()