# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 9. OOP Pillar: Abstraction

print("\n --- Introduction --- ")
print(" -------------------- \n")
#
# When a program starts to get big, classes might start to share functionality
# or we may lose sight of the purpose of a class's inheritance structure. In
# order to alleviate issues like this, we can use the concept of abstraction.
#
# Abstraction helps with the design of code by defining necessary behaviors 
# to be implemented within a class structure. By doing so, abstraction also
# helps avoid leaving out or overlapping class functionality as class
# hierachies get larger.

from abc import ABC, abstractmethod
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED

class Animal(ABC):
  def __init__(self, name):
    self.name = name
  
  @abstractmethod
  def make_noise(self):
    pass
  
class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
  
class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))

kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise()
doggy.make_noise()

# Above we have Cat and Dog classes that inherit from Animal. The Animal
# class now inherits from an imported class ABC, which stands for 
# Abstract Base Class.
#
# This is the first step to making Animal an abstract class that cannot
# be instantiated. The second step is using the imported decorator
# @abstractmethod on the empty metho .make_noise()
#
# The below line of code would throw an error.

#an_animal = Animal("Scruffy")
# TypeError: Can't instantiate abstract class Animal with abstract method
# method make_noise

# The abstraction process defines what an Animal is but does not allow the 
# creation of one. The .__init__() method still requires a name, since we
# feel all animals deserve a name.
#
# The .make_noise() method exists since all animals make some form of noise,
# but the method is not implemented since each animal makes a different noise.
# Each subclass of Animal is now required to define their own .make_noise()
# method or an error will occur.
#
# These are some of the ways abstraction supports the design of an organized
# class structure.


print("\n --- Tasks --- ")
print(" ------------- \n")
#
# 1. Take a look at the code in script.py. The abstract class AbstractEmployee
#    is defined. It has all the logic that has previously existed in the 
#    Employee class, except that the .say_id() method is not implemented and
#    has the @abstractmethod decorator.
#
#    The Employee class currently has no implementtation.
#
#    Run the code and observe that e1.say_id() is causing an AttributeError
#    since the Employee class has no implementation.
#
# 2. Let's fix this error:
#
#     - Make the Employee class inherit from the AbstractEmployee class
#
# 3. Nice work! But wait, there's still an error!
#
#    TypeError: Can't instantiate abstract class Employee with abstract
#    methods say_id
#
#    The .say_id() method in the AbstractEmployee class uses the @abstractmethod
#    decorator. This means any class that inherits from AbstractEmployee must
#    implement a .say_id() method.
#
#    Inside the Employee class replace the pass statement, then:
#
#     - Define a say_id() method that outputs a message with self.id
#
#    When complete you should see the output in the console.


#from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1
  
  @abstractmethod
  def say_id(self):
    pass
  
  
class Employee(AbstractEmployee):
  def say_id(self):
    print("My ID is {}.".format(self.id))
  
e1 = Employee()
e1.say_id()