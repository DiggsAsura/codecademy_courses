# 8. Resource Management
# 1. Context Managers
# 10. Review

# Congratulations! We have reached the end of the context managers lesson. Making 
# it this far means that we have explored mandy of the core concepts behind
# context managers. Let's recap:
#
# *Context Manager:
#
# - Context managers are a form of resource managment in python invoked by the 
#   with statement.
#
# - They ensure that resource are closed/released after usage regardless of
#   whether or not an error occurs. 
#
# - They can be created from scratch using either the class-based method or the
#   contextlib decorator-based method.
#
# - Behind every context manager, there's an __enter__ and __exit__ method 
#   taking place. 
#
# - Context managers can be nested together to work with resources simultaneously.
#
#
# *Class-Based Context Managers:
#
# - They can be created from scratch with the manual implementation of the __enter__
#   and __exit__ method.
#
# - The __exit__ method takes three arguments (+ self): An exception type, an 
#   exception value and traceback. The method can then handle exceptions.
#
# 
# *Decorator Based Context Managers:
#
# - They can be created from scratch using the contextlib contextmanager decorator
#   on a generator function
#
# - In the contextlib method, the except block handles exception's code block
#
#
# To explore context managers further, check out the Python Documentation:
# https://docs.python.org/3/library/contextlib.html#module-contextlib


print('No tasks')