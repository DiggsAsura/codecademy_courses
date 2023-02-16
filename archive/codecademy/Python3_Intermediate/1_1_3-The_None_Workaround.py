# Learn Intermediate Python 3
# 1. Function Arguments
# 3. The None Workaround

# If we want an empty list as a potential default argument value, we can 
# use None as a special value to indicate we did not receive anything. After
# we check wheter an argument was provided, we can instantiate a new list 
# if it wasn't. Here is what the solution looks like for our 
# program earlier:

def createStudent(name, age, grades=None):
  if grades is None:
    grades = []
  return {
    'name': name,
    'age': age,
    'grades': grades
  }

def addGrade(student, grade):
  student['grades'].append(grade)
  print(student['grades'])
  
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

addGrade(chrisley, 90)
addGrade(dallas, 100)

# Ok I wonder if this course is a bit early for me to really see the big
# benefit of. I mean, I do understand the workaround - I just have some
# problems to relate to the problem it is a solution for. 

# While it may seem more cumbersome to write the if clause, this is one of
# the most common (and flexible) ways to avoid running into issues with 
# mutable default arguments. Let's practice by refactoring the last 
# assessment code. 

# Quiz:
# Fill in the following code to account for the mutable default arguments
# Python gotcha.
#
# The expected output of the solution is:
# [{'item': 'soda', 'cost': '1.50'}]

def update_order(new_item, current_order=None):
  if current_order is None:
    current_order = []
  
  current_order.append(new_item)
  return current_order

order1 = update_order({'item': 'burger', 'cost': '3.50'})
order2 = update_order({'item': 'soda', 'cost': '1.50'})

print(order2)

# Boom, got it. Lol. 



# Wrap up:

# To summarize, we learned:
#   - What a Python gotcha is
#   - What mutable objects are in Python 
#   - A common gotcha that occurs when using mutable default arguments.
#   - A workaround for mutable default arguments by using None paired with 
#     a conditional statement.
#
# Keep this gotcha in mind whenever deciding to use a mutable object as a
# default argument. While most developers recommend staying away from this
# approach, there are notable use cases for this syntax that may be worth
# looking into. 