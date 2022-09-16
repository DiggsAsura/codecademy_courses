# 8. Resource Management
# 1. Context Managers
# 4. Class Based Context Managers II

print('\nClass Based Context Managers II\n')

# Now that we know the structure of implementing our own class-based context
# manager. Let's walk through a context manager that manages actual files as
# well as explore each of the methods we saw earlier. Here is what our context
# manger will look like:

class WorkWithFile:
  def __init__(self, file, mode):
    self.file = file
    self.mode = mode
  
  def __enter__(self):
    self.opened_file = open(self.file, self.mode)
    return self.opened_file

  def __exit__(self, *exc):
    self.opened_file.close()

# We have written a class-based context manager called WorkWithFile! Let's break
# down each method and what happens inside of it.
#
#   - The __init__ method:
#
#     This method is standard across most classes, even ones that are not context
#     manager themselfs. In this case, we have three parameters:
#
#       1. self: This is standard for any class we work with and allow us to 
#          work with methods and properties we assign to an instance of a class.
#
#       2. file: Since we are working with files, we need to be able to take in
#          a file argument when we call the glass with a with statement.
#
#       3. mode: Lastly, we need to provide the file a mode. This allows us to
#          manage what our context manager will actually be doing, such as
#          reading, writing, or both!
#
#     Both file and mode arguments allow us to accomplish the following syntax:
#!     with WorkWithFile('file.txt', 'r')
#
#   - The __enter__ method:
#
#     This is where we deal with opening the file we want to work on. Since any 
#     new instance of our context manager will have a file and mode property,
#     we can pass them into the open() function to open a specific file with
#     a specific mode. Then, we save it as a variable called self.open_file,
#     and return it.
#
#     By returning self.open_file, the file will be passed into the variable
#     we define when we call it with the with statement. So for example:
#!     with WorkWithFile('file.txt', 'r') as file
#
#     Will assign the open file 'file.txt' to the variable called file that 
#     follows the as clause and thus allowing us to use it in the with statement
#     code block (which we will look at shortly).
#
#   - The __exit__ method:
#
#     Lastly, but one of the most important steps, we have to close the file we
#     work on. Here we are still taking in a *exc argument, but we won't touch
#     on that until the next exercise. For now, this method is solely responsible
#     for closing the resource we opened in __enter__.
#
# Now that we created our context manager, we can now use it in a with statement
# like so:

with WorkWithFile("file.txt", 'r') as file:
  print(file.read())

# Okay, here we go:
# 
# 1. The with statement executes and a context manager object is created from the
#    class provided, with the values of the arguments required in the init
#    method.
#
# 2. The enter method is run.
#
# 3. The enter method opens the file and returns a handle (refrence) to the target
#    variable file in the with statement. This is why in the method we return
#    self.opened_file.
#
# 4. Then the code block in the with statement executes; printing the contents
#    of the file to the console.
#
# 5. Once the code in the with statement is completed, The exit method is called.
#
# 6. The exit method closes the file.
#
#
# Phew, these context managers are a handful! Take some time to let it all sink
# in, then let's create our own context manager that works on poem files!

print('\nTasks\n')

# 1. Let's build our poem context manager from earlier again! This time we will
#    allow it to work on files. By the end of these exercises, we will have
#    a custom context manager that has written to a file!
#
#    Create a class called PoemFiles and git it a __init__ method that defines
#    a self, poem_file and a mode parameter.
#
#    Inside the method, print 'Starting up a poem context manager'
#
# 2. Next, let's build the properties of the class via __init__. Remember
#    this is so we can pass a file anme and a mode when we call the context 
#    manager with the with statement.
#
#    Inside of the __init__ method and under the print statement, assign two
#    properties to the class:
#
#     - file that is equal to the poem_file parameter
#
#     - mode that is equal to the mode parameter
#
# 3. Next, let's work on the __enter__ method to set up what happens when we
#    want to start working on a file.
#
#    Create an __enter__ method. Have the method print 'Opening poem file'.
#
# 4. In the __enter__ method, we will need to open the file we want to work on
#    and return it! This way, it will be assigned to the variable we declare 
#    when we work with the with statement. 
#
#    Inside __enter__ method give the class a new property called opened_poem_file
#    and assign it to a call of the open() function that takes two arguments:
#
#     - self.file: our classes file property
#
#     - self.mode: our classes mode property
#
#    Lastly, return the opened_poem_file property!
#
# 5. Lastly, we need to create an __exit__ method.
#
#    Write a __exit__ method that defines a self parameter and a *exc parameter.
#    Make the method print 'Closing poem file'.
#
# 6. We need to make sure we close our file in the __exit__ method so we
#    properly manage our resources.
#
#    In the __exit__ method, under the print statement, call the .close()
#    built-in function on the opened_poem_file property of the class.
#
# 7. Uncomment the with statement and run the code. Check out poem.txt to see
#    if the poem has been added!
#
#    Note: in reality, we wouldn't have to create a context manager that opens a
#    file because there's already an open() built-in function that you can run 
#    with a with statement that will open and close a file. However, open() has 
#    its limitations, and knowing this base structure will allow us to create
#    our own custom and more advanced context managers that can do much more
#    than open()!

class PoemFiles:
  def __init__(self, poem_file, mode):
    print('Starting up a poem context manager')
    self.file = poem_file
    self.mode = mode
  
  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file
  
  def __exit__(self, *exc):
    print('Closing poem file')
    self.opened_poem_file.close()
  
with PoemFiles('poem.txt', 'w') as open_poem_file:
  open_poem_file.write('Hope is the thing with feathers')