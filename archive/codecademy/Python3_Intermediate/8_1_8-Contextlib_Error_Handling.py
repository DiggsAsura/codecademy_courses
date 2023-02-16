# 8. Resource Management
# 1. Context Managers
# 8. Contextlib Error Handling

print('\nContextlib Error Handling\n')

# In the previous exercise, we explored how to create a context manager using
# the contextlib module. However, we did not go over how to deal with errors just
# as we did with the class-based approach. Like any other pattern, you may run into
# errors when invoking your context manager using the @contextmanager decorator.
#
# For the class-based context manager, the __exit__ method dealt with exceptions.
# For the decorator method, errors are most commonly dealt with within and except
# block. We will build on top of our try/finally block by incorporating an except.
# There are two main ways to deal with errors:
#
# - To throw an error and stop the execution of our entire program, we can:
#     - Simply do nothing by excluding an except block
#
# - To catch erros and continue the execution of our program, we can:
#     - Handle the exception via an except block.
#
# Let's look at an example of what a decorator based context manager that catches
# errors can look like:

from contextlib import contextmanager

@contextmanager
def open_file_contextlib(file, mode):
  open_file = open(file, mode)

  try:
   yield open_file

  except Exception as exception:
   print('We hit an error: ' + str(exception))

  finally:
   open_file.close()

with open_file_contextlib('file.txt', 'w') as opened_file:
  opened_file.sign('We just made a context manager using contextlib')
  
# Notice: 
#
#   - The inclusion of the except clause
#
#   - The except attempts to catch a generic Exception and, if it is hit, saves
#     it to a variable exception.
#
#      - Note: we can use any exception object, not just a generic one, if we know
#        the specific exception we are tryingt o catch.
#
#   - The handler prints out the error
#
# When this context manager is called in the with statement above, it will hit the
# exception block because .sign() is not a file method. The output would look like
# this:

#! We hit an error: '_io.TextIOWrapper' object has no attribute 'sign'

# This tells us what our error is, so we know what to fix. Now, let's practice
# upgrading our poem_files context manager to catch exceptions.


print('\nTasks\n')

# 1. Let's add an except clause to the poem_files context manager so that it
#    catches an AttributeError exception, saves it as variable called e.
#
#    Print e inside of the except block.
#
# 2. Let's see our exception handling in action! Uncomment the with statement
#    block and run code.

#! from contextlib import contextmanager

@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
    
  except AttributeError as e:
    print(e)
  
  finally:
    print('Closing File')
    open_poem_file.close() 
    
with poem_files('poem.txt', 'a') as opened_file:
  print('Inside yield')
  opened_file.sign('Buzz is big city. big city is buzz.')