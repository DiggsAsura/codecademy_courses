# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 5. Custom Iterators I

print('''\n
Custom Iterators I
--------------------- ''')
# We have seen that the methods __iter__() and __next__() must be implemented
# for an object to be an iterator object. The implementation of these methods
# is knwon as the iterator protocol.
#
# If we desire to create our own custom iterator class, we must implement the
# iterator protocol, meaning we need to have a class that defines at 
# minimum the __iter__() and __next__() methods.
#
# To look at a scenario where we might require our own custom iterator, imagine
# we are receiving a shipment of new fish that we can now sell in our pet store.
# We don't have any classes to manage our fish inventory, so we need to create
# a custom class to do so. If we wanted to track the available fish inventory,
# our custom class initializer may look something like this:

#!class FishInventory:
#!  def __init__(self, fishList):
#!    self.available_fish = fishList

# By default, custom classes are not iterable. We can't just go around plugging
# our custom classes into for loops and expecting any results! This presents a
# problem if the class are working with needs the ability to iterate.
#
# When we reate a FishInventory class object, we want to iterate over all the
# fish available within self.available_fish. If we attempt to directly
# iterate over our custom FishInventory class object, we will receive an error
# because we have not yet implemented the iterator protocol for this custom
# class. To make the FishInventory class iterable, we can simply define
# __iter__() and __next__() methods.
#
# Defining these methods is discussed in the next exercise, but first, let's
# see what happens if we attempt to iterate our FishInventory class
# object directly.

################

print('''\n
Tasks
----------- ''')
# 1. Try and iterate over our FishInventory class object, fish_inventory_cls,
#    to see all the available fish we have.
#
#    Create a for loop to iterate over the fish_inventory_cls object and run
#    the code.

class FishInventory:
  def __init__(self, fishList):
    self.available_fish = fishList

fish_inventory_cls = FishInventory(["Bubbles", "Finley", "Moby"])

for fish in fish_inventory_cls:
  print(fish)