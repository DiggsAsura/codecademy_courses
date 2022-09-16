# Chapter 11 - Classes
# 1. Introduction to Classes
# 13. String Representation

# One of the first things we learn as programmers is how to print out
# information that we need for debugging. Unfortunately, when we print out
# an object we get a default representation that seems fairly useless. 
#
#class Employee():
#    def __init__(self, name):
#        self.name = name
#        
#argus = Employee("Argus Filch")
#print(argus)
#
# This default string representation gives us some information, like where 
# ther class is defined and our computer's memory address where this object
# is stored, but it's usually not useful information to have when we 
# are trying to debug our code. 
#
# We learned about the dunder method __init__(). Now, we will learn another
# dunder method called __repr__(). This is a method we can use to tell 
# Python that we want the string representation of the class to be. 
# __repr__() can only have one parameter, self, and must return a string. 
#
# In our Employee class above, we have an instance variable called name that
# should be unique enough to be useful when we're printing out an instance of
# the Employee class. 
#
from numpy import round_


class Employee():
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self.name

argus = Employee("Argus Filch")
print(argus)
#
# We implemented the __repr__() method and had it return the .name attribute
# of the object. When we printed the object out it simply printed the .name
# of the object! Cool!

# Tasks
# 1. Add a __repr__() method to the Circle class that returns
#    Cicle with radius {radius}
#
# 2. Print out medium_pizza, teaching_table and round_room.

class Circle:
    pi = 3.14
    
    def __init__(self, diameter):
        self.radius = diameter / 2
    
    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius
    
    def __repr__(self):
        return "Circle with radius {radius}".format(radius=self.radius)

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

# Classes kinda start to open up. This __repr__() looks convenient too!
# Still have to get alot of practice on this. 
#
# Plan is to get through the course, get the basic chapters. Maybe do another
# course or re-run/speed run this whole Course once more to really try 
# to get down the foundation. Before starting to code too much on my own. 
# Ref, started a small rpg, before knowing of vital basic stuff lol. 
