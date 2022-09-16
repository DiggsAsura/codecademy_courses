# 6. Iterators & Generators
# 3. Generators
# 2. yield vs return

# Generator functions are similar to regular functions except that they must
# return an iterator. But instead of using a return statement, generator
# functions use an expression called yield. 
#
# So how does yield differ from a return statement? Well, any code that is
# written after a yield expression will execute on the next iteration of
# the iterator. Code written after a return statement will not execute.
#
# The following example shows how the yield expression is used within a
# generator function:

def course_generator():
  yield 'Computer Science'
  yield 'Art'
  yield 'Business'

print(course_generator())

for i in course_generator():
  print(i)
  
# This function will return an iterator that contains the string values 'Computer
# Science', 'Art' and 'Business'. On each iteration of the iterator, each yield
# will return its corresponding course value.
#

courses = course_generator()
for course in courses:
  print(course)

# Would print out:

#! Computer Science
#! Art
#! Business

# Another key difference between yield and return is that the yield expression
# will suspend the execution of the function and preserve any local
# variables that exist within the function. The return statement will terminate
# the function immediately and return the result(s) to the caller.
#
# Like all objects, the iterator object returned by a generator function can be
# stored in a variable to be used later on. It can then be iterated through as 
# needed.
#
# Let's utilize the yield keyword to write our own generator function!

# Tasks
# 1. We want to create a generator that will generate values of class
#    standings: 'Freshman', 'Sophomore', 'Junior', and 'Senior'. The generator
#    function should be named class_standing_generator.
#
# 2. Initialize an iterator object called class_standings from calling
#    class_standing_generator()
#
# 3. Use a for loop to iterate through the class_standings iterator to print
#    out each class standing value.
#
####

def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

class_standings = class_standing_generator()

for standing in class_standings:
  print(standing)