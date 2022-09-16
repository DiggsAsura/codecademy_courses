# 6. Iterators & Generators
# 3. Generators
# 6. Generator Methods: throw()

from re import I


print('\nGenerator Methods: throw()')
#
# The generator method throw() provides the ability to throw an exception inside
# the generator from the caller point. This can be useful if we need to end
# the generator once it reaches a certain value or meets a particular condition.
#
# Using the throw() method looks like this:

#!def generator():
#!  i = 0
#!  while True:
#!    yield i
#!    i += 1
#!
#!my_gen = generator()
#!for item in my_gen:
#!  if item == 3:
#!    my_gen.throw(ValueError, "Bad value given")

# To see how throw() method can be used in a real-world scenario, let's 
# practice using it some more.

###

print('\nTasks ---\n')
# 1. We have a collection of 5,000 students.
#
#    We only want to retrieve information on the first 100 students. Use the
#    throw() method to throw a ValueError of "Invalid student ID" if the 
#    iterated student ID goes over 100. Insert your code before the
#    print(student_id) line. 

def student_counter():
  for i in range(1, 5001):
    yield i

student_generator = student_counter()

for student_id in student_generator:
  if student_id == 101:
    student_generator.throw(ValueError, "Invalid student ID")
  print(student_id)