# 6. Iterators & Generators
# 3. Generators
# 9. Generator Pipelines

print('\nGenerator Pipelines -----')
# Generator pipelines allow us to use multiple generators to perform a series of 
# operations all within one expression. We can break down complex operations
# into smaller, more manageable parts where they can then be pipelined together
# to achieve the desired output.
#
# To pipeline generators, the output of one generator function can be the input
# of another generator function. That resulting generator can then be used as
# input for another generator function, and so on.
#
# Pipeline generators are also often referred to as nested generators. We can
# use a pipelined generator like in the following example:

def number_generator():
  i = 0
  while True:
    yield i
    i += 1
 
def even_number_generator(numbers):
  for n in numbers:
    if n % 2 == 0:
      yield n
 
even_numbers = even_number_generator(number_generator())
 
for e in even_numbers:
  print(e)
  if e == 100:
    break

# The above example contains:
#
#   - The infinite generator number_generator() that yields numbers 
#     incrementing by 1.
#
#   - The infinite generator even_number_generator() which takes a generator 
#     as a parameter, iterates through that generator and only yields even
#     numbers.
#
#   - The even_numbers variables which holds an even_number_generator() as 
#     its argument.
#
# When we iterate over even_numbers only even numbers are output. The 
# even_number_generator() iterates over all numbers using number_generator().
# When an even number occurs, that number is returned by even_number_generator().
#
# Let's practice more with generator pipelines!


print('\nTasks -----')
# 1. We have three courses:
#
#     - Computer Science which have 5 students
#
#     - Art which has 10 students
#
#     - Business which has 15 students
#
#    First, complete the generator function called course_generator that can
#    yield tuples of (Course name, Number students) for the above courses
#    and corresponding number of students. The first tuple for Computer Science
#    has been provided.
#
# 2. We need to add 5 students to each course. Create a generator function 
#    called add_five_students that takes in an input variable called courses.
#    This courses object contains tuples of (Course name, Number of students).
#    The add_five_students generator function should loop through the courses
#    input object.
#
#    On each iteration, it should yield a tuple containing the course name and
#    number of students plus 5. The resulting generator that is yielded should
#    have the following values:
#
#     - Computer Science with 10 students
#
#     - Art with 15 students
#
#     - Business with 20 students
#
# 3. Use a pipeline generator (nested generator) to get the resulting generator
#    that has the 5 added students to each course. Set it to a variable called
#    increased_courses.
#
#    Print out each course tuple in the resulting increased_courses generator
#    using a for loop.


def course_generator():
  yield ("Computer Science", 5)
  yield ("Art", 10)
  yield ("Business", 15)

def add_five_students(courses):
  for course, num_students in courses:
    yield (course, num_students + 5)

increased_courses = add_five_students(course_generator())

for course in increased_courses:
  print(course)


  