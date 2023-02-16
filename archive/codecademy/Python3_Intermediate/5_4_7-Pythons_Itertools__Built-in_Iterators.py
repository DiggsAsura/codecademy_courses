# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 7. Python's Itertools: Built-in Iterators

# Python's Itertools: Built-in Iterators
#
# While building our own custom iterator classes can be useful, Python offers
# a convenient, built-in module named itertools that provides the ability
# to create complex iterator manipulations. These iterator operations can input
# either a single iterable or a combination of them.
#
# There are three categories of itertool iterators:
#
#! Infinite:
#   Infinite iterators will repeat an infinite number of times. They will not
#   raise a StopIteration exception and will require some type of stop 
#   condition to exit from.
#
#! Finite
#   Finite iterators are terminated by the input iterable(s) sequence length.
#   This means that the smallest length iterable used in a finite iterator
#   will terminate the iterator
#
#! Combinatoric:
#   Combinatoric iterators are iterators that are combinational, where mathematical
#   functions are performed on the input iterable(s).
#
# We can use the itertools module by simply supplying an import statement at 
# the top of the module like this:

#! import itertools

# While we will only cover specific itertools for each three of these itertools
# types, the full list of itertools can be found in the official Python
# documentation: https://docs.python.org/3/library/itertools.html

#!  Infinite      #!  count()        #! These iterators repeat an infinite number
#!  Iterators     #!  cycle()        #! of times and require some type of stop
#                 #!  repeat()       #! condition to exit from.
#
#*  Finite        #*  chain()        #* These iterators are terminated by the
#*  Iterators     #*  compress()     #* input iterator(s) sequence length.
#                 #*  filterfalse()
#
#?  Combinatoric  #? product()       #? Iterators in which combinational
#?  Iterators     #? permutations()  #? mathematical functions are performed on.
#                 #? combinations()


# Help me. lol.