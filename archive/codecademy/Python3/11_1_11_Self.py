# Chapter 11 - Classes
# 1. Introduction to Classes
# 11. Self

# Since we can already use dictionraies to store key-value pairs, usint objects for 
# that purpose is not really usefull. Instance variables are more powerful when you
# can guarantee a rigidity to the data the object is holding.
#
# This convenience is most apparent when the constructor creates the instance 
# variables, using the arguments passed in to it. If we were creating a search engine,
# and we wanted to create classes for each separate entry we could return. We'd do that
# like this:
#class SearchEngineEntry:
#	def __init__(self, url):
#		self.url = url	
#codecademy = SearchEngineEntry("www.codecademy.com")
#wikipedia = SearchEngineEntry("www.wikipedia.org")
#print(codecademy.url)
#print(wikipedia.url)
#
# Since the self keyword refers to the object and not the class being called, we can 
# define a secure method on the SearchEngineEntry class that returns the secure link 
# to an entry.

class SearchEngineEntry:
	secure_prefix = "https://"
	def __init__(self, url):
		self.url = url
	
	def secure(self):
		return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
print(wikipedia.secure())
#
# Above we define our secure() method to take just the one required argument, self.
# We access both the class variables self.secure_prefix and the instance varialbe
# self.url to return a secure URL. 
#
# This is the strength of writing object-oriented programs. We can write our classes
# to structure the data that we need and write methods that will interact with 
# that data in a meaningful way.

# Tasks
# 1. In script.py you'll find our familiar friend, the Circle class.
# 
# 	 Even though we usually know the diameter beforhand, what we need for most 
#	   calculations is the radius. 
#
# 	 In Circle's constructor set the instance vaiable self.radius to equal half 
# 	 the diameter that gets passed in.
#
# 2. Define three Circle's with three different diameters:
# 		- A medium pizza, medium_pizza, that is 12 incehs across. 
# 		- Your teaching table, teaching_table, which is 36 inches across.
# 		- The Round Room, round_room, which is 11,460 inches across. 
#
# 3. Define a new method circumference for your circle object that takes only one
# 	 argument, self, and returns the circumference of a circle with the given 
# 	 radius by this formula:
# 	 circumference = 2 * pi * radius
#
# 4. Print out the circumferences of medium_pizza, teaching_table, and round_room.

class Circle:
	pi = 3.14
	def __init__(self, diameter):
		print("Creating circle with diameter {d}".format(d=diameter))
		self.radius = diameter / 2
		
	def circumference(self):
		return 2 * self.pi * self.radius
	
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# hmmm allmost understand, but not quite.. gotta practice this quite a bit. 

