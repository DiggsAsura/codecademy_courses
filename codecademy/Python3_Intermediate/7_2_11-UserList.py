# 7. Specialized Collections
# 2. Collections
# 11. UserList

print('\nUserList\n---------------')

# Not only can we create our own version of a dictionary, the UserList wrapper
# container lets us create our own list as well! This class contains all of the 
# functionality of a regular list, but it also has a property called data which
# allows us to access the list contents directly. Here is an example of a 
# modified list using the container wrapper:

from collections import UserList

# Create a class which inherits from the UserList class
class CondenseList(UserList):
  
  # A new method to remove duplicate items from the list
  def condense(self):
    self.data = list(set(self.data))
    print(self.data)
  
  # We can also owerwrite a method from the list class
  def clear(self):
    print("Deleting all items from the list!")
    super().clear()

condense_list = CondenseList(['t-shirt', 'jeans', 'jeans', 't-shirt', 'shoes'])

condense_list.condense()
condense_list.clear()

# As shown in this code example, we can add additional methods and overwrite
# methods from the UserList class. This is the same as inheriting from regular
# classes in Python.
#
# Let's try creating our own list class!


print('\nTasks\n------------')

# 1. Now, let's try creating a custom list class using UserList. Create a new
#    class called ListSorter which inherits from the UserList class. Inside of
#    this class, overwrite the .append() method to sort the list after 
#    appending the value to it.
#
# 2. Now that we have created our own list class, try creating an object using
#    it's constructor. Create an object called sorted_list and pass data
#    into the ListSorter constructor. Afterwards, append the value 2 to the
#    new object and print out the results. 

data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

#!from collections import UserList

class ListSorter(UserList):
  def append(self, item):
    self.data.append(item)
    self.data.sort()
  
sorted_list = ListSorter(data)
sorted_list.append(2)
#sorted_list.append('kayi') # Nope, can't mix. Thought I could.

print(sorted_list)