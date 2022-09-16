# 8. Resource Management
# 1. Context Managers
# 5. Handling Exceptions I

print('\nHandling Exceptions I\n')

# Remember this?

#! def__exit__(self, *exc):

# It's time to address the big mystery. What in the world is the *exc parameter in 
# the __exit__ method we have been writing so far?
#
# Well, context managers play an important role in handling exceptions. Recall
# exceptions are errors that happen within the runtime of a code, terminating
# it before its completion. Within a context manager, the __exit__ method is 
# responsibile for dealing with any exceptions. It can implement how to close the
# file and any other operations we want to perform if an exception occurs.
#
# So far, we have been using *exc to fill in the argument requirements for our
# context managers __exit__ method. If we went back and wrote this instead:

#! def __exit__(self):

# We would have been met with a puzzling error:

#! __exit__() takes 1 positional argument but 4 were given.

# This is because the __exit__ method needs four total arguments! In the past
# exercises, we ignored this requirement by using the * operator to tell the
# method we will pass a variable number of arguments even though we never did.
# It was a good way to put the above error on hold, but now let's dive into what
# these required arguments are and how to use them so that we can master the
# __exit__ method.
#
# The __exit__ method has three required arguments (in addition to self):
#
#   1. An exception type: which indicates the class exception (i.e. AttributeError
#      class, or NameError class)
#
#   2. An exception value: the actual value of the error
#
#   3. A traceback: a report detailing the sequence of steps that caused the error
#      and all the details needed to fix the error.
#
# Let's take a look at an example context manager that deals with exceptions in its
# __exit__ method:

class OpenFile:
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
  
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file
  
  def __exit__(self, exc_type, exc_val, traceback):
    print(exc_type)
    print(exc_val)
    print(traceback)
    self.opened_file.close()

# In this __exit__ method, we are dealing with exceptions by adding a script that
# prints the exception values to the console. We can see the outcome of our simple 
# exception handling when we run our with statement with an intentional failure:

#!with OpenFile("file.txt", "r") as file:
  # .see() is not a real method
#!  print(file.see())

# Would output:

#! <class 'AttributeError'>
#! '_io.TextIOWrapper' object has no attribute 'see'
#! <traceback object at 0x705dfslf23o> 

# Once the with statement is run, we get the above message that tells us that we have
# AttributeError, that our object has no attribute 'see', and provides a traceback
# object. When an error occurs, the code stops, and resources (i.e., file in our
# earlier example) are still closed. The values of these three arguments are then
# thrown or suppressed.
#
# In contrast, if no error occurs in the with statement above, the __exit__
# method would have printed:

#! None
#! None
#! None

# Note that exc_type, exc_value and traceback are completly arbitary names. We can
# use any name we want for these parameters as long as it does not hinder the
# readability of our code. In general, it's best practice to be as descriptive
# as possible!
#
# Now, let's experience exceptions in context managers for ourselves.


print('\nTasks\n')

# 1. Let's return to our trusty PoemFiles context manager. Unfortunately, it's 
#    missing an __exit__ method. Now that we have seen how to set up the method
#    to capture exception data, let's build it out.
#
#    Create an __exit__ method, and add the 4 necessary arguments: self, 
#    exc_type, exc_value, traceback. Have the method use 3 different print statements
#    to print each exception argument. This will help us visualize the 
#    exceptions when we run into them!
#
# 2. As the last part of our __exit__ method, use the .close() built-in function
#    to close the opened_poem_file property.
#
# 3. Looks like our context manager is complete. Time to see it in action!
#
#    Uncomment the first (marked #First) commented out with call that attempts
#    to print the contents of our poem.txt file in all uppercase.
#
#    Run the code and observe the exception data that comes up!
#    Can you spot the error?
#
# 4. Looks like we ran into a small error in the last step! In particular, we ran
#    into an AttributeError because .uppercasewords() isn't a real method.
#
#    Now let's see what happens in our program when we don't run into an error.
#    Comment out the first with statement we just ran and uncomment the second one
#    (marked # Second).
#
#    Run the code and observe the exception data that comes up! In the next
#    exercises, we'll learn how to customize our exception handling to better
#    work with errors that appear in our code. 

class PoemFiles:
  
  def __init__(self, poem_file, mode):
    print('\n -- Starting up a poem context manager -- \n')
    self.file = poem_file
    self.mode = mode
  
  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file
  
  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    self.opened_poem_file.close()

with PoemFiles('poem.txt', 'r') as file:
  print(file.read())
  print("---- Exception data below -----")