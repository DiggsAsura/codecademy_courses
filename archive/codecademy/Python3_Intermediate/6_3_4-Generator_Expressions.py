# 6. Iterators & Generators
# 3. Generators
# 4. Generator Expressions

print('\nGenerator Expressions\n')
# Generator expressions allows for a clean, single-line definition and creation
# of an iterator. By using a generator expression, there is no need to define
# a full generator function as we covered in the previous exercises.
#
# Generator expressions resemble the syntax of list comprehensions. However,
# they do differ in the following ways:

#? Generator Expressions                     List Comprehensions
#? Returns a newly defined iterator          Returns a new list
#? Uses parantheses                          Uses Brackets

# Let's look at an example of how the two compare:

#! List comprehension
a_list = [i*i for i in range(4)]

#! Generator comprehension
a_generator = (i*i for i in range(4))

# In this code above, a_list will be a list object containing the values
# [0, 1, 4, 9]. The object a generator will be a generator object that 
# cannot be accessed directly like a_list. It will need to be traversed
# to retrieve the values it contains. To show this further, we can print
# out a_list and a_generator and see what is returned:

print(a_list)
print(a_generator)

# Output:
#![0, 1, 4, 9]
#!<generator object <genexpr> at 0x7f82e0e4d4c0>

# Since our generator expression returns an iterator object, we can loop through
# to obtain the values within it:

for i in a_generator:
  print(i)

# Output:
#!0
#!1
#!4
#!9

# We can practice more with generator expressions by using them to create some
# new college courses!

####
print('\nTasks\n')
#
# 1. Given the defined generator function cs_generator(), retrieve a generator
#    object by calling cs_generator() and set it to a variable called cs_courses.
#    Print out the values within the iterator using a for loop.
#
# 2. After the for loop, create an iterator using a generator expression and
#    put it in a variable called cs_generator_exp. The iterator should 
#    produce the same output as cs_generator()
#
# 3. Print out the values of the cs_generator_exp iterator object using
#    a for loop. The output should match the for loop print output of 
#    iterating over cs_courses.

def cs_generator():
  for i in range(1, 5):
    yield "Computer Science " + str(i)

cs_courses = cs_generator()

for i in cs_courses:
  print(i)


cs_generator_expression = (f'Computer Science {i}' for i in range(1, 5))

for i in cs_generator_expression:
  print(i)