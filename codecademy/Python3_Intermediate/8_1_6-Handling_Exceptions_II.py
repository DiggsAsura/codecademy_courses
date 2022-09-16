# 8. Resource Management
# 1. Context Managers
# 6. Handling Exceptions II

print('\nHandling Exceptions II\n')

# Printing exceptions isn't the only way we can handle them in the __exit__ method.
# An exception that occurs in a context manager can be handled in two ways:

#   - If we want to throw an error when an error occurs, we can either:
#     - Return False after the .close() method
#     - Do nothing
#
#   - If we want to supress the error, we can:
#     - Return True after the .close() method
#
# Using a script similar to our earlier example, we can examine how this works:

class OpenFile:
 
 def __init__(self, file, mode):
   self.file = file
   self.mode = mode
 
 def __enter__(self):
   self.opened_file = open(self.file, self.mode)
   return self.opened_file
 
 def __exit__(self, exc_type, exc_val, traceback):
   print(exc_type, exc_val, traceback)
   print("The exception has been handled")
   self.file.close()
   return True

# Notice above that nothing changed except for adding of return True to implement
# suppression of an error. To see this in action, we'll call two with statments using
# this context manager;
# One that will thwo an exception and another that will not. Let's obvserve the 
# behavior:

#with OpenFile("file.txt", "r") as file:
# print(file.see())

#!with OpenFile("file.txt", "r") as file:
#! print(file.read())

# When we run this code, our output is as follows:

#! <class 'AttributeError'>
#! '_io.TextIOWrapper' object has no attribute 'see'
#! <traceback object at 0x7fedf822d180>
#!
#! The exeption has been handled
#!
#! None None None

# Here we see that:
#
#   - The error message we manually code is printed but there is no automatic
#     error message thrown by the program.
#
#   - Both with statements ran.
#
# If we did not return True, the second (and all proceeding) with statements would
# not have run since an exception would be hit.
#
# Additionally, we can choose to handle a specific exception, while also suppressing
# it! This is useful if we want our context manager to not block the execution
# of other code, but also customize the output if a certain exception occurs. Here
# is an example of working with a TypeError:

class OpenFile2:
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
  
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file
  
  def __exit__(self, exc_type, exc_val, traceback):
    if isinstance(exc_value, TypeError):
      print("The exception has been handled")
      return True
    self.file.close()

# Notice the if statement that compares exc_value to a specific exception we are
# trying to catch. Anything we want to happen for this specific exception can
# occur in the conditional code block. Lastly, we return True to make sure
# we suppress the exception from arising and stopping the rest of our code from
# running.
#
# Let's return to our poem context manager from earlier and implement some 
# exception handling!

print('\nTasks\n')

# 1. We are back with our PoemFile context manager!
#
#    There are currently two with calls. Run the code to see what exception
#    occurs. In the next step, we will try handle it!
#
# 2. Looks like our AttributeError is back in our first with call.
#
#    Inside of the __exit__ method, write a conditional using the isinstance() 
#    function to check if the exception is an AttributeError. If it is, close
#    the file and return True!

class PoemFiles:
  
  def __init__(self, poem_file, mode):
    print('\n -- Starting up a poem context manager --\n')
    self.file = poem_file
    self.mode = mode
  
  def __enter__(self):
    print('\n -- Opening poem file -- \n')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file
  
  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback)
    if isinstance(exc_value, AttributeError):
      self.opened_poem_file.close()
      return True
    

with PoemFiles('poem.txt', 'r') as file:
  print("--- Exception data below --- \n")
  print(file.uppercasewords())

with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print(" \n --- Exception data below --- \n")
  