# 8. Resource Management
# 1. Context Managers
# 3. Class Based Context Managers

print('\nClass Based Context Managers')

#Now that we have an understanding of why we need tonctext managers and the
# power of the with statement, it is essential for us to know what's happening
# under the hood to gain a much deeper understanding of the concept. The best
# way to see the internal workings of a concept manager (such as the with 
# statement) is by creating our own!
#
# One of the two approaches of creating context managers is referred to as the
# clsas-based approach. The class-based approach of writing context managers 
# requires explicitly defining and implementing the following two methods
# inside of a class:
#
# - An __enter__ method:
#
#   - The __enter__ method allows for the setup of context managers. This method
#     commonly takes care of opening resources (like files). This method also
#     begins what is known as the runtime context - the period of time in which
#     a script runs. In our previous examples, it was the time in which the code
#     passed into the with statement code block was executed (basically 
#     everything under the with statement)
#
# - An __exit__ method
#
#   - The __exit__ ensures the breakdown of the breakdown of the context manager.
#     This method commonly takes care of closing open resources that are no 
#     longer in use.
#
# To visualize these methods and the approach, let's take a look at a custom
# class-based context manager below:

class ContextManager:
  def __init__(self):
    print('Initializing class....')
  
  def __enter__(self):
    print('Entering context...')
  
  def __exit__(self, *exc):
    print('Exiting context...')

# Here, we defined a new class called ContextManager (to be extra explicit) and
# implemented the required methods. By defining these two methods, we are 
# implementing the context management protocol - a guideline for the required
# methods for a context manager. Don't get too caught up in the arguments
# passed to each method, we will talk through them in the next exercises, but
# they are required to not experience an error.
#
# Implementing the context management protocol allows us to immediatly invoke
# the calss using the with statement as shown below:

with ContextManager() as cm:
  print('Code inside with statement')

# The above shows that our context manager class is executed in the following
# sequence:
#
# 1. __init__ method
# 2. __enter__ method
# 3. The code in the with statement block
# 4. __exit__ method
#
# Let's practice getting down the basicas of writing a class-based context manager
# in addition to the execution flow before diving deeper into the __enter__ and 
# __exit__ methods.
#

print('\nTasks\n')

# 1. Let's create a context manager that will work with files filled with
#    creative poems. While we won't directly work with a file in this exercise,
#    make sure to note the order of method execution in a context manager. Don't
#    worry, we'll work with an actual file soon! For now, we are just going to get
#    comfortable with the basics.
#
#    Create a class called PoemFiles. For now, give it a single pass statement
#    so it won't create an error when run.
#
# 2. Next, remove the pass statement and create an __init__ method inside of the
#    PoemFiles class that prints 'Creating Poems!'
#
# 3. Let's implement the __enter__ method. Have the method print 'Opening
#    poem file'.
#
# 4. Lastly, create an __exit__ method that prints 'Closing poem file'.
#
# 5. Awesome! Now we have our very own context manager! Let's see it in action
#    by calling it with a with statement.
#
#    Have the with statement save the invoked class to a variable called 
#    manager and have it print a famous line from the poet Emily Dickinson:
#    'Hops is the thing with feathers'.

class PoemFiles:
  def __init__(self):
    print('Creating Poems!')
  
  def __enter__(self):
    print('Opening poem file')
  
  def __exit__(self, *exc):
    print('Closing poem file')


with PoemFiles() as manager:
  print('Hope is the thing with feathers')