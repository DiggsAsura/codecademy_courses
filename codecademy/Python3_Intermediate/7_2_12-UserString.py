# 7. Specialized Collections
# 2. Collections
# 12. UserString

print('\nUserString\n----------------')

# Since strings are also considered containers, the collections module also 
# provides a container wrapper for the string class. This contains all of the 
# functionality of a regular string, but it includes the string's data inside
# of a property called data. Inheriting from this class allows us to create our
# own version of a string! Here is an example:

from collections import UserString

class IntenseString(UserString):
  def exclaim(self):
    self.data = self.data.upper() + '!!!'
    return self.data

  # Overwrite the count method to only count a certain letter
  def count(self, sub=None, start=0, end=0):
    num = 0
    for let in self.data:
      if let == 'P':
        num += 1
    return num

intense_string = IntenseString('python rules')

print(intense_string.exclaim())
print(intense_string.count())

# This shows how we can add additional methods to the original container's class
# or even overwrite existing methods. This is the same as inheriting from regular
# classes in Python.
#
# Now let's create our own string class!


print('\nTasks\n------------')

# 1. Now let's create a new string class using UserString. Import the UserString
#    class and create a new class called SubtractString which inherits from it.
#    In this class, overwrite the - operator to remove the string on the right
#    side of the operator from the string stored in the object. Another way
#    to think about this is to replace the substring on the right side of the
#    operator with an empty string.
#
# 2. Now that we have created our new string class, create a new object from that
#    class called subtract_string while passing str_name in as the argument
#    to the constructor. Next, use the - operator to subtract the substring
#    str_word from subtract_string.


str_name = 'python powered patterned products'
str_word = 'patterned'

#! from collections import UserString

class SubtractString(UserString):
  def __sub__(self, other):
    if other in self.data:
      self.data = self.data.replace(other, '')

subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)