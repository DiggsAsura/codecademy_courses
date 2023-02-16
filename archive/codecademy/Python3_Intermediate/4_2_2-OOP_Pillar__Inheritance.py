# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 2. OOP Pillar: Inheritance

# When we haear the word "inheritance", code may not be the first thing that 
# springs to mind; we're probably more likely to think of inheriting genetic 
# traits, like the eye color from a mother or dimples from a grandfather.
# In the world of Object-Oriented Programming, inheritance is actually
# one of the core pillars for creating intricate structurs with our classes.
# To dive into this concept, let's examine a Dog and Cat class:

#class Dog:
#  def bark(self):
#    print('Woof')
  
#class Cat:
#  def mewo(self):
#    print('Meow')

# These two classes define two distinct animals with their own methods of 
# communication. Now, what if we wanted to give both of these classes the
# ability to eat by calling a method called eat(). We could write the method
# twice in both classes but then we would be repeating code! We also may
# need to write it inside every specific animal class ever created. Instead,
# we can utilize the power of inheritance.
#
# Since both Cat and Dog fall under the classification of Animal we can 
# create a parent class to represent properties and methods they can both 
# share! Her is what it might look like:
print("\n --- Example --- \n")
class Animal:
  def eat(self):
    print("Nom Nom Nom... eating food")

# Great, we have an Animal class with a eat() method, but how do we actually
# get the Dog and Cat class to inherit this method so it can be shared with
# both classes? Well here is what the base structure will look like:

#class ParentClass:
  #class methods/properties...
  
#class ChildClass(ParentClass):
  #class methods/properties...

# If we apply this structure to our example, our code looks like this:

class Dog(Animal):
  def bark(self):
    print('Bark')

class Cat(Animal):
  def meow(self):
    print('Meow')

# Now, let's see inheritance in action:

fluffy = Dog()
zoomie = Cat()

fluffy.eat()
zoomie.eat()

# Output
# Nom Nom Nom... eating food
# Nom Nom Nom... eating food

# As we can see, there are some clear advantages of utilizing inheritance. Not
# only are we able to reuse methods across multiple classes using our parent
# class, but we are also able to create parent-child relationships between
# entities!

print("\n --- Tasks --- \n")
# =============================

# 1. Now that there is an Employee class we want to make a more specific type
#    of employee, Admin.
#
#    In script.py:
#     - Create an Admin class that inherits from the Employee class
#     - Inside the body of the class insert the pass statement
#
# 2. Now it's time to tet out your inheritance implementation
#
#    At the bottom of your script.py:
#     - Define a variable e3 and set it to an instance of the Admin class
#
#    Now if you call the .say_id() method on the Admin instance in e3, you 
#    will get output with the instance's id. 

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
    
  def say_id(self):
    print("My id is {}.".format(self.id))
    
class Admin(Employee):
  pass

e1 = Employee()
e2 = Employee()
e3 = Admin()

e3.say_id()

# I do know this, but it's nice to go a bit in depth on it! This is
# undoubtly some cruicial tings to keep in mind when coding OOP. 