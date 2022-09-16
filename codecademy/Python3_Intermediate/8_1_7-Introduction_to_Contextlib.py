# 8. Resource Management
# 1. Context Managers
# 7. Introduction to Contextlib

print('\nIntroduction to Contextlib\n')

# We learned that we can create our own context managers using the class-based
# method, but there's an even simpler way of creating context managers. We
# can use a built-in Python module called contextlib!
#
# The contetlib module allows for the creation of a context manager with the
# use of a generator function (a function that uses yield instead of return) and
# the contextlib decorator - @contextmanager. Instead of creating a class and
# defining __enter__ and __exit__ methods, we can use a simple function!
#
# There are a few steps in the setup so let's take it slow and break down each
# step. First, we will need to import the built-in module  into our script and
# grab the @contextmanager decorator:

from contextlib import contextmanager

# Once we have successfully imported the module, we can automatically use the
# @contextmanager decorator to wrap a simple generator function:

@contextmanager
def open_file_contextlib(file, mode):
  opened_file = open(file, mode)
  try:
    yield opened_file
  finally:
    opened_file.close()

# We are doing a few things here:
#
#   1. We have written a generator function called open_file_contextlib with the
#      expectation that it takes in a file as a single argument
#
#   2. We use the built-in open() function to open the file (that we received
#      as an argument) and save it to a variable called opened_file
#
#   3. The function then will attempt (via a try statement) to yield the opened
#      file and complete whatever code we pass when we use it in conjunction
#      with the with statement. More on this in a bit!
#
#   4. Lastly the resource (file) will be closed once all the code is done
#      being executed
#
# If we think about this structure in sections relative to the class-based
# approach, it essentially breaks down into this:

#!@contextmanager
#!def generator_functions(<parameters>):
#!  <setup section - equivalent to __enter__>
#!  try:
#!    yield <value>
#!  finally:
#!    <cleanup section - equivalent to __exit__>

# Once we have created this function and denoted it as a context manager using the
# @contextmanager decorator, we can immediatly use it like before in a with
# statement:

with open_file_contextlib('file.txt', 'w') as opened_file:
  opened_file.write('We just mada context manager using contextlib')

# Follow this pattern of creating context managers allows us to quickly convert
# generator functions to become context managers without the need to create any
# extra classes. Now, lets remake our poem context manager following this pattern!


print('\nTasks\n')

# 1. Let's create our PoemFiles context manager from previous exercises. First, 
#    import contextmanger from contextlib
#
# 2. Now, let's create a generator function called poem_files that has two
#    parameters file and mode. This function should do two things:
#
#     1. Print 'Opening File'
#
#     2. Open the file using open() with the file and mode parameter, and save
#        the result to a variable called open_poem_file
#
#    Don't forget to decorate it with the @contextmanager decorator.abs
#
# 3. Next, we will have to create the try/finally structure. Inside of the function
#    write  the try clause, and inside of it use the yield keyword to yield the
#    open_poem_file variable
#
# 4. Now, let's finish the try/finally block by writing a finally clause that 
#    does two things:
#
#     1. Print 'Closing File'
#
#     2. Call close() on the open_poem_file variable.
#
# 5. Uncomment and run the with statement below your script.

#! from contextlib import contextmanager

@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()

with poem_files('poem.txt', 'a') as opened_file:
  print('Inside yield')
  opened_file.write('\nRose is beautiful, Just like you.')