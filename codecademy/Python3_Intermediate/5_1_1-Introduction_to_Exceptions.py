# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 1. Introduction to Exceptions

print('''\n
Introduction to Exceptions
---------------------------- ''')
# It is truly an amazing feeling when our code works exactly the way we want
# it to. On the other hand, it can be equally frustrating when our code runs
# into errors. Since errors are such an integral part of working with Python,
# it's important to know how to control errors and use them for our advantage
# effectively. In this lesson, we will explore a specific type of error, 
# an exception.
#
# At this point, we are probably very familiar with the most common type of
# error: a syntax error. Syntax errors are mistakes in the structure of
# Python code. They are caught during a special parsing stage before a program
# is executed. They always prevent the entire program from running. For 
# example, here is the error output of a syntax error:

#! File "script.py", line 1
#!   def print five
#!                ^
#! SyntaxError: invalid syntax

# As opposed to a syntax error, an exception is a different kind of error that
# can occur with syntactically correct code. Exceptions are runtime errors
# because they occur during program execution, only when the offending code
# (the code causing the error) is reached. An example of an exception, and one
# we have probably seen before, is a NameError:

#! Traceback (most recent call last):
#! File "script.py", line 1, in <module>
#!   print(five)
#! NameError: name 'five' is not defined

# Although the NameError has a similar output to a SyntaxError (both end with
# Error), it falls under the category of exceptions. Exceptions and syntax
# errors make up the two core categories for any error we will run into.

#                    Python Errors
#       Syntax Errors               Exceptions 

# We'll encounter many different kinds of exceptions, some of which will be
# unfamiliar. Luckily, as we saw in the example above, Python gives us a tool
# for gaining insight into exceptions - the traceback. A traceback is a 
# summary that includes the exception type, a message, and the series of
# function calls preceding the exception, along with file names and line
# numbers. Here is another example of a traceback for a small program:

#! print(1/0)

#! Traceback (most recent call last):
#! File "script.py", line 1, in <module>
#!   print(1/0)
#! ZeroDevisionError: division by zero

# In the traceback above, reading from the bottom line, we see the exception 
# type (ZeroDivisionError) followed by a message (division by zero). Going up,
# we see that the exception orginated on line 1 of a file called script.py while
# calling print(1/0). We'll be using tracebacks throughout the rest of the 
# lesson to track and identify why and where our exceptions are occuring.
#
# Let's get some practice debugging syntax errors and exceptions. For this
# lesson, let's imagine we are hired by Instrument World, a musical instrument
# company with retail and online stores.

print('''\n
Tasks
------- ''')
# 1. Take a look at the code in welcome.py. There is a syntax error on line
#    3 (the extra closing paranthesis).
#
#    Will any of the previous code be executed? Press "Run" to find out.
#
# 2. Fix the error from the extra closing paranthesis from line 3. Run the
#    code to see what happens.
#
# 3. We hit an exception on line 3 because of the misspelled variable name!
#    However, the previous lines of code were executed (observe Welcome to
#    in the output) because exceptions occur at runtime.
#
#    Fix the variable name on line 3 to continue!

#print('Welcome to')
#store = 'Instrument World'
#print(stor))

print('Welcome to')
store = 'Instrument World'
print(store)
