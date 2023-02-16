# Learn Intermediate Python 3
# 1. Function Arguments
# 1. Python Gotcha: Mutable Default Arguments

# Gotcha meaning
# When you expect a return and get something else - when the code apparently 
# is correct. It's a counterintuitive feature of a programming language that
# often leads to mistakes in programs. 

def createStudent(name, age, grades=[]):
  return {
    'name': name,
    'age': age,
    'grades': grades
  }

kenneth = createStudent('Kenneth', 37)
kayi = createStudent('Ka Yi', 30)

def addGrade(student, grade):
  student['grades'].append(grade)
  print(student['grades'])
  
addGrade(kenneth, 90)
addGrade(kayi, 100)
# Output is
# [90]
# [90, 100]
# Why was kayi returned like this? Gotcha!

# This task is a quiz.
# What is the output of the following code?

def update_order(new_item, current_order=[]):
  current_order.append(new_item)
  return current_order

order1 = update_order({'item': 'burger', 'cost': '3.50'})
order2 = update_order({'item': 'soda', 'cost':'1.50'})

print(order2)

# correct guess:
# [{'item': 'burger', 'cost': '3.50'}, {'item': 'soda', 'cost':'1.50'}]

# I don't fully understand it. It get's mutated of course. Order1 will 
# be normal, but order2 will mutate with order1. How to avoid this? 