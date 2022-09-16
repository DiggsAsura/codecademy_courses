# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 6. Custom Iterators II

print('''\n
Custom Iterators II
----------------------- ''')
# To iterate over a custom class we must implement the iterator protocol by
# defining the __iter__() and __next__() methods. In most cases the two
# methods can do the following:
#
#   - The __iter__() method must always return the iterator object itself.
#     Typically, this is accomplished by return self. It can also include
#     some class member initializing.
#
#   - The __next__() method must either return the next value available
#     or raise the StopIteration exception. It can also include any number
#     of operations.
#
# Let's return to our custom FishInventory class:

class FishInventory:
  def __init__(self, fishList):
    self.available_fish = fishList

# We want to make the FishInventory class iterable to see all the available fish.
# To make it iterable, we first define the __iter__() method. We can initialize
# a class member within the __iter__() method called index that will help us
# track the current position we're in within the self.available_fish list.

  def __iter__(self):
    self.index = 0
    return self

# Notice that the __iter__() method returns itself since this class will be an
# iterator object. The __iter__() method can return other iterator objects, but
# typically the object itself is returned here by using return self.
#
# Then, we define the __next__() method. Recall that we can perform operations
# inside this method, like incrementing class members or traversing a for loop 
# for instance.

#!  def __next__(self):
#!    fish_status = self.available_fish[self.index] + "is availble!"
#!    self.index += 1
#!    return fish_status

# We return the next available fish status within a string value and increment
# our class member index by 1.
#
# Iterating over this class object will eventually error out since we fail to do
# any checking of our index value against the length of the self.available_fish
# list. We can avoid this and cleanly stop the iterator by raising the
# StopIteration exception in our __next__() method. Here, we'll modify our
# __next__() method to raise StopIteration if index exceeds the length of
# available_fish.

  def __next__(self):
    if self.index < len(self.available_fish):
      fish_status = self.available_fish[self.index] + "is available!"
      self.index += 1
      return fish_status
    else:
      raise StopIteration

# Let's practice implementing the iterator protocol in a custom class!


print('''\ 
Tasks
-------------- ''')
# 1. Imagine we have a custom class called CustomerCounter that counts the number 
#    of customers in the store. Make this class iterable by first defining the
#    __iter__() method. Within this method, initialize a class member called
#    self.count that will keep count of the number of customers in the store.
#
# 2. Next, define the __next__() method. Only 1 customer will enter at a time
#    each time this __next__() method is called.
#
# 3. Create a class instance customer_counter from the CustomerCounter class.
#
# 4. If we were to iterate through the customer_counter object using a for 
#    loop now, we would get an infinite loop since our __next__() method
#    has not raised a StopIteration exception.
#
#    Let's fix this by moving on to Step 5 where we can raise this exception
#    and prevent an infinite loop from occuring!
#
# 5. Modify the __next__() method to raise a StopIteration exception when our
#    customer count si greater than 100.
#
# 6. Create a for loop to iterate through our CustomerCounter class object
#    customer_counter. Print out each customer count value on each loop
#    iteration.
#
#############

class CustomerCounter:  
  def __iter__(self):
    self.count = 0
    return self
  
  def __next__(self):
    if self.count > 100:
      self.count += 1
      return self.count
    else:
      raise StopIteration

customer_counter = CustomerCounter()

for customer in customer_counter:
  print(customer)
  
  
# How the f do I get it to actually print?