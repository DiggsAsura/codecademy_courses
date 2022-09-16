# Learn Intermediate Python 3
# 6. Iterators & Generators
# 3. Generators
# 1. Introduction to Generators

# In Python, a generator allows for the creation of iterators without having to 
# impelemtn __iter__() and __next__() methods. Generators improve code readability,
# save memory by allowing for iterative access of elements, and allow for the 
# traversal of infinite streams of data. 
#
# There are two types of generators in Python:
#
#   1. Generator functions
#
#   2. Generator Expressions
#
# Both of these return a generator object that can be looped over similar to a list, 
# but unlike a list, the contents of the generator object are not stored in
# memory, allowing for complex and even infinite iteration of data.
#
# Defining generator function will resemble how we already define regular
# functions, except for a few key components that we will dive into in the 
# following exercises.


# Generator funtions                       Generator Expressions
#
#        Yield                          Generator1()     Generator2()
#                                         output           output
#                   
# Generator1() Generator2()                       Generator3()
#    yields       yields
#
#        Generator3()                       Generator Methods
#           yields