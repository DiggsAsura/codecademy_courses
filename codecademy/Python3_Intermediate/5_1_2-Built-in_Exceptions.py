# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 2. Built-in Exceptions

print('''
Built-in Exceptions
-------------------- ''')

# In the previous exercise (and probably many times before), we saw one type of
# exceptions called the NameError. The NameError is just one of many built-in
# exceptions - exceptions that are built into the Python language. Other built-in
# exceptions cover fields ranging from mathematical errors all the way to 
# operating system errors. We don't need to memorize them all, but it's helpful
# to be familiar with some common ones and, more importantly, understand
# where they come from inside Python.
#
# Exceptions are objects just like anything else. Most exceptions inherit directly
# from a class called Exception; however, they are all derived directly or indirectly
# from the BaseException class. We can examine the base classes by using the
# __bases__ atrribute on any specific exception:

print(NameError.__bases__)

# Will output:
# (<class 'Exception'>,)

# We can even call __bases__ on the Exception class to see its origins:

print(Exception.__bases__)

# Will output:
# (<class 'BaseException'>,)

# The full hierarchy of built-in exceptions is the following:

'''
BaseException
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- AritheticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |     +-- BrokenPipeError
      |    |     +-- ConnectionAbortedError
      |    |     +-- ConnectionRefusedError
      |    |     +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |    |     +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |    |     +-- UnicodeDecodeError
      |    |     +-- UnicodeEncodeError
      |    |     +-- UnicodeTranslateError
'''

# Note that there is a lot of exceptions built into the language of Python. Again,
# we don't need to memorize all of them, but at some point, we may see them pop
# up in our programs. We can find details on each of the exceptions listed in
# the Python documentation.
#
# Later in this lesson, we'll be using the Exception base class to create custom
# exceptions. For now, let's get some practice encountering built-in
# exceptions and reading their tracebacks

print('''\n
Tasks 
--------''')

# Tasks
# 1. Instrument World has a program that prints some of the most
#    popular instruments it has on sale. 
#
#    Take some time to look over the program, and then run the code in 
#    instruments.py. We'll encounter another exception that we might not have
#    seen before. What might this exception be telling us?
#
# 2. Take a look over traceback - it ends with the exception type and a brief
#    message. Above that is the exact line that caused the exception.
#
#    Fix this line so that the exception no longer occurs and then re-run
#    the code.
#
# 3. Looks like the exception we saw in the previous step was a TypeError.
#    Let's confirm which base class it is derived from.
#
#    Use print() to output a TypeError.__bases__.
#
# 4. There is another exception that gets hit - once again, read the traceback,
#    fix the exception, and re-run the code.

#!sale_instruments = ['Violin', 'Conga', 'Clavinet']
#!print('The following ' + len(sale_instruments) + ' instruments are on sale:')
#!print(sale_instruments[0])
#!print(sale_instruments[1])
#!print(sale_instruments[3])

sale_instruments = ['Violin', 'Conga', 'Clavinet']

#print(TypeError.__bases__)

print('The following ' + str(len(sale_instruments)) + ' instruments are on sale:')
print(sale_instruments[0])
print(sale_instruments[1])
print(sale_instruments[2])