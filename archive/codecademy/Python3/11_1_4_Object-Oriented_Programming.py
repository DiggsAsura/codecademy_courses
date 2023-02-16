# Chapter 11 - Classes
# 1. Introduction to Classes
# 4. Object-Oriented Programming

# A class instance is also called an object. The pattern of defining classes and 
# createing objects to represent the responsibilities of a program is known as 
# Object Oriented Programming or OOP. 
#
#
# Instantiation takes a class and turns it into an object, the type() functions
# does the opposite of that. When called with an object, it returns the class that 
# the object is an instance of. 

#print(type(cool_instance))
# prints "<class '__main__.CoolClass'>" 
#
# We print out the type() of cool_instance and it shows us that this object is 
# one type __main__.CoolClass.
#
# In Python __main__ means "this current file that we're running" and so one could
# read the output from type() to mean "the class CoolClass that was defined 
# here, in the script you're currently running."

# Tasks 
# 1. In script.py we see facade_1 from last exercise. Try calling type() on 
# 	 facade_1 and save it to the variable facade_1_type
#
# 2. Print out facade_1_type

class Facade:
	pass
	
facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)
