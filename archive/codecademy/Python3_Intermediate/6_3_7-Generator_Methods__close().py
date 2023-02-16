# 6. Iterators & Generators
# 3. Generators
# 7. Generator Methods: close()

from re import I


print('\nGenerator Methods: close()\n')
# The generator method .close() is used to terminate a generator early.
# Once the .close() method is called the generator is finished just like
# the end of a for loop. Any further iteration attempts will raise a
# StopIteration exception.

def generator():
  i = 0
  while True:
    yield i
    i += 1

my_gen = generator()
next(my_gen)
next(my_gen)
my_gen.close()
#!next(my_gen) # raises StopGenerator Exception

# In the above example, my_gen() holds an infinite generator object. After a 
# couple next(my_gen) calls, my_gene.close() is called. When we attempt to 
# call next(my_gen) again, a StopIteration exception is raised.
#
# The .close() method works by raising a GeneratorExit exception inside the
# generator function. The exception is generally ignored but can be handled
# by using try and except.

def generator2():
  i = 0
  while True:
    try:
      yield i
    except GeneratorExit:
      print("Early exit, BYE!")
      break
    i += 1

my_gen2 = generator2()
for item in my_gen2:
  print(item)
  if item == 1:
    my_gen2.close()

#! Output:
#!0
#!1
#!Early exit, BYE!

# Putting the yield expression in a try block we can handle the GeneratorExit
# exception. In this case, we simply print out a message. Because we interrupted
# the automatic behavior of the .close() method, we must also use a break
# to exit the loop or else a RuntimeError will occur.
#
# To practice this further, we can attempt to use the .close() method on 
# our student generator.
#
##


print('\nTasks -----\n')
# 1. We have a collection of 5,000 students. We only want to retreive information
#    on the first 100 students. Use the close() method to terminate the generator
#    after 100 students. 

def student_counter():
  for i in range(1, 5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  if student_id == 100:
    student_generator.close()
