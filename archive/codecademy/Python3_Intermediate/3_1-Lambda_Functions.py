# Learn Intermediate Python 3
# 3. Functions Deep Dive
# 1. Lambda Functions

# (This chapter is slightly different laid out)

# Learn how to define a Python function in one line!
#
# In Python, a lambda function (also commonly called an anonymous
# function) is a one-line shorthand for function. Let's start by 
# examining how lambda functions compare to the normal functions
# we have already been writing.
#
# Take for example, a function called add_two():
#def add_two(my_input):
#  return my_input + 2
#
# The same function could be writting as a lambda function:
#add_two = lambda my_input: my_input + 2
#
# So this code using the above lambda function:
#print(add_two(3))
#print(add_two(100))
#print(add_two(-2))
#
# Output:
# 5
# 102
# 0
#
# Let's break this syntax down:
#
# 1. This function is stored in a variable called add_two
# 2. The lambda keyword declares that this is a lambda function (similar
#    to how we use def to declare a normal function)
# 3. my_input is a parameter used to hold the value passed to add_two
# 4. In the lambda function version, we are returning my_input + 2 without
#    the use of a return keyword (the normal Python function explicitly uses 
#    the keyword return)
#
# Let's practice identifying a conversion from a normal function to a lambda 
# function!

# Multiple Choice Question:
# Which of the following is a proper conversion of the function below into 
# a lambda function?
#
#def add_bang(sentence):
#  print(sentence + "!")
#add_bang = lambda string: print(string + "!") 

# Correct :)

# Our lambda functions can be more complex than the above example. For 
# instance, let's say we want a function that will perform differently
# based on different inputs. 
#
# Let's say that we have a function check_if_A_grade that outputs 
# 'Got an A!' if a grade is at least 90, and otherwise says you 'Did not
# get an A.'. So, the code:
# We can do this using a conditional if statement in a lambda function, with
# syntax that looks like this:
#check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'
#print(check_if_A_grade(91))
#print(check_if_A_grade(70))
#print(check_if_A_grade(20))
#
# Output:
# Got an A!
# Did not get an A.
# Did not get an A.
#
# This is what our line of code does:
# 1. lambda grade: declares a lambda function with the parameter grade
# 2. Return 'Got an A' if this statement is true: grade >= 90
# 3. Otherwise, return 'Did not get an A.'
#
# Lambda functions are the preferred way of creating one-line functions. The
# reduced syntax assists code readability and the functions can be implemented
# where code reuse is not the primary objective. If we wanted our function
# complexity to extend beyond one line, we would opt for a regular function
# since making our function longer would impair readability.
#
# Now we can make simple Python functions in one line! Let's get some
# practice in!

# Fill in the Code
# Fill in the blanks to complete a lambda function named double_or_zero
# that takes an integer named num. If num is greater than 10, return double
# the value of num. Otherwise, return 0.
double_or_zero = lambda num: num*2 if num>10 else 0
print(double_or_zero(5))
print(double_or_zero(11))