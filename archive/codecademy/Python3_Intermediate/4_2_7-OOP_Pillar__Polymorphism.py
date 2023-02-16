# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 7. OOP Pillar: Polymorphism

print("\n --- Introduction --- ")
print(" -------------------- \n")

# In computer programming, polymorphism is the ability to apply an identical
# operation onto different types of objects. This can be useful when an
# object type may not be known at the program runtime. Polymorphism can be
# applied using Python in multiple ways. We have already experienced a form
# of it when exploring inheritance.

class Animal: 
  def __init__(self, name):
    self.name = name
    
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))

class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
  
class Robot:
  def make_noise(self):
    print("beep.boop....BEEEEP!!!")

# The example above shows an Animal class, its subclass Cat, and another 
# standalone class Robot. Each class has a method .make_noise() with different
# outputs. The identical method name with different behaviors is a form
# of polymorphism.

an_animal = Animal("Bear")
my_pet = Cat("Maisy")
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]

for o in objects:
  o.make_noise()
#
# Output:
# Bear says, Grrrr
# Maisy says, Meow!
# bee.boop....BEEEEP!!!

# With the classes instantiated and added to a list, we are able to iterate
# through the list and call .make_noise(). This is done without needing
# to know what type of class .make_noise() belongs to.

print("\n --- Tasks ----")
print(" -------------- \n")
# 
# 1. A meeting needs to be scheduled with at least one employee, one admin and 
#    one manager.
#
#     - Define a variable meeting and set it equal to a list that contains
#       an instance of each class, Employee(), Admin() and Manager()
#
# 2. With the different types of employees in the meeting, have them all
#    say their ID. 
#
#     - Using a for loop iterate through the list meeting
#
#     - Using your defined loop varialbe, call .say_id() method
#       on each instance in the list

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
  
  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")
    
meeting = [Employee(), Admin(), Manager()]

for m in meeting:
  m.say_id()