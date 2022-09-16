# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 1. Introduction to Object-Oriented Programming

# In programming, most languages offer various features that give us
# different ways to tackle technical problems. With so many different languages
# out there, it became necessary to create a classification system to help 
# distinguish those sets of features. This ultimately led to the creation
# of the term programming paradigm - a way to classify different programming
# languages and the unique features that they offered. 
#
# As we explore Python deeper, our code might fall into multiple paradigm
# categories at once. This is because most modern-day languages offer
# more than one specific paradigm we can program in. While we could spend
# all day exploring all the paradigms Python offers, we will instead dive
# into one of the most popular paradigms, and one we have already been 
# using (maybe unknowingly), called Object-Oriented Programming (OOP).
#
# At the forefront of any language classified as OOP language, there must
# exist the ability to create programs around classes and objects. We have
# already started working with these concepts earlier as we built or own
# custom classes, class methods, and instance objects. To recap, let's take
# a look at an example:
#class Dog:
#  sound = "Woof"
#  
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age
#  
#  def bark(self):
#    print(Dog.sound)
#
# In the above example, we are representing a real-world entity (a dog) as
# a class with properties (name and age) and methods (bark). These features
# make up for the core of the OOP paradigm and ultimately allows us to build
# more intrecate programs. This however only scratches the surface of what we
# we can accomplish. To explore the paradigm further, we will examine the
# four core pillars of OOP:
#
# 1. Inheritance
# 2. Polymorphism
# 3. Abstraction
# 4. Encapsulation
#
# Each of these pillars will allow us to expand our skills so that we can take
# full advantage of the power of object-oriented programming in Python! We 
# will begin exploring these pillars in later exercises but for now, let's 
# refresh ourselfs on OOP fundamentals.

#
# Tasks
# 
# 1. To start our exploration into OOP, create a class that will represent an 
#    employee of a company. 
#    
#    In script.py:
#     - Define the Employee class with an __init__() method
#     - Define a class variable new_id and set it to 1
#
# 2. Each employee instance will need its own unique ID. 
# 
#    Inside the Employee class:
#     - Define an __init__() method
#     - Inside __init__(), define self.id and set it equal to the class variable
#       new_id
#     - Lastly, increment new_id by 1
#
# 3. Now create a function to output the instance id.
#
#    Inside the Employee class:
#     - Define a say_id() method
#     - Inside say_id(), output the string "My id is " and then the instance ID.
#
# 4. Lastly, create 2 employees and have them give their id's. 
#
#    Outside of the Employee class:
#     - Define the variable e1 and set it to an instance of Employee
#     - Define the variable e2 and set it to an instance of Employee
#     - Have both e1 and e2 output their IDs

class Employee:
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
  
  def say_id(self):
    print("My id is " + str(self.id))

e1 = Employee()
e2 = Employee()
e1.say_id()
e2.say_id()   
  
#instance_variable = Class_Name()
#instance_variable.method_name()
