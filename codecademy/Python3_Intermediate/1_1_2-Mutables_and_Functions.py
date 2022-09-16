# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Mutables and Functions

# To understand this gotcha, we must first establish 
# what Python classifies as mutable. A mutable object refers to various
# containers in Python that are intended to be changed. A list for example
# has append and remove operations that change the elements of the list.
# Sets and dictionaries are also two other mutable objecs in Python as
# they can change on the fly. 
#
# It might be helpful to note some of the objects in Python that are not
# mutable (and therfore OK to use as default arguments). int, float, and 
# other numbers can't be mutated (arithmetic operations will return a new 
# number). Tuples are a kind of immutable list, and strings are also 
# immutable since operations that update a string will all return
# a completly new string. 
# 
# When using a mutable in function arbuments, it's important to note
# the following (from the official documentation):
#
# "Default parameter values are evaluated from left to right when the 
# function definition is executed. This means that the expression is 
# evaluated once, when the function is defined, and that the same
# "pre-computed" value is used for each call."
#

def createStudent(name, age, grades=[]):
  return {
    'name': name,
    'age': age,
    'grades': grades
    }
  
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

def addGrade(student, grade):
  student['grades'].append(grade)
  print(student['grades'])
  
addGrade(chrisley, 90)
addGrade(dallas, 100)

print(id(chrisley['grades']))
print(id(dallas['grades']))
# prints
# 139828567365696
# 139828567365696

# WTH is this ID, where does it come from? ugh... This is hard.

# Note: The ids printed will vary depending on the computer we are using 
# (yea i have something else) but they will always be the same!
#
# While this may seem like a bit of a headscratcher (you dont say..), and
# even a point of contention among Python enthusiasts, thre is one specific
# solution that helps us get around this gotcha if we ever do want to use a 
# mutable default argument. Let's take a look at a solution that uses the 
# value None to get around this gotcha.

