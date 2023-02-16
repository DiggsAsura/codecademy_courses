# 8. Resource Management
# 1. Context Managers
# 2. A Familiar Face: The with Statement

print('\nA Familiar Face: The with Statement')

# One of the most common ways to manage resources in Python is to make sure the
# files we use in our scripts are properly closed after use.
#
# We already explored this concept when we used the with statement when operating
# on files. The with statement is the most common and pythonic way to invoking
# context managers in python. This means we have been using the concept of
# context managers all along!
#
# Let's recap how to use a with statement:

with open("file_name.txt", "w") as file:
  file.write("How you gonna win when you ain't right within?")

# Here is what happening in our small script:
#
# 1. The with statement calls the built-in open() function on "file_name.txt"
#    with a mode of "w" which represents write mode.
#
# 2. The as clause assigns the object opened (the file) to a target variable
#    called file, which can be accessed inside of the context manager (scope?)
#
# 3. file.write() writes a sentence to "file_name.txt"
#
# But, what exactly does this have to do with resource management? In order to 
# answer this question, we need to take a peek behind the curtain and 
# examine what our code looks like without a with statement. Here is what the
# same code would look like without the use of a context manager like with:

file = open("file_name.txt", "w")
try:
  file.write("How you gonna win when you ain't right within?")
finally:
  file.close()

# The alternative to using with would require us to manually open (using open()
# and close() the file we are working on. By using the with statement in the first
# example, it serves as a context manager where files are automatically closed
# after script completion and we don't ever have to worry about the possibility
# of forgetting to close a resource. Remember, leaving our resources open
# will hog up our finite computer resources. We are never guaranteed that Python
# will close the file for us if we happen to forget to do it!
#
# In the next exercise, we'll dive deeper into how context managers like the with
# statement are built. For now, let's start using it and seeing its power 
# compared to the alternative try/finally clauses.
#

print('\nTasks\n')

# 1. Take a look at the code in the text editor. Notice that the file was
#    opened but never closed. This is bad practice and could lead to errors
#    down the road.
#
#    Update this script by:
#
#     - Putting the code that opens the file inside a try block
#
#     - Closing open_file in a finally block using .close()
#
# 2. Now rewrite this script in with statement form using open_file as the 
#    target vaiable. Use the "r" mode for read permissions.


with open("file_name.txt", "r") as open_file:
  print(open_file.read())
