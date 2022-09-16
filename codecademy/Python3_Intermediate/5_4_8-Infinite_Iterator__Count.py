# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 8. Infinite Iterator: Count

# An infinite iterator will repeat an infinite number of times with no endpoint
# and no StopIteration exception raised. Infinite iterators are useful when we 
# have unbounded streams of data to process.
#
# A useful itertool that is an infinite iterator is the count() itertool.
# This infinite iterator will count from a first value until we provide some
# type of stop condition. The base syntax of the funciton looks like this:

#! count(start,[step])

# The first argument of count() is the value where we start counting from. The
# second argument is an optional step that will return current value + step. The
# step value can be positive, negative, and an integer or float number. It will
# always default to 1 if not provided.
#
# To show how it's used in a scenario, suppose we want to quickly count up and
# print all even numbers from 0 to 20.

# We first import the itertools module and then create a loop (this can be
# a while loop or a for loop), that will iterate through our count() iterator:

#!import itertools

#!for i in itertools.count(start=0, step=2):
#!  print(i)
#!  if i >= 20:
#!    break

# Here is what happens in the script:
#
#   - We set our start argument to 0 so that we can start counting from 0
#
#   - We set our step argument to 2 so that way we increment +2 on each
#     iteration.
#
#   - We create a stop condition, which is i >= 20, otherwise this for loop
#     would continue printing forever!
#
# And our output becoms
#! 0
#! 2
#! 4
#! .....
#! 20

# Let's use the count() itertool to manage our pet store!

###
# Tasks
#####
# 1. We have several 13.5lb bags of dog food to display. Our single shelving
#    unit however can only hold a maximum of 1,000lbs. Let's figure out how
#    many bags of food we can display!
#
#    First, import the itertools module at the top line of the code editor.
#
# 2. Next, initialize a for loop with a count() iterator that keeps track of
#    the weight on the shelf.
#
#    Within the for loop body:
#
#     - Provide a stop condition using max_capacity to terminate the loop
#
#     - Increment num_bags on each iteration
#
# 3. Print the num_bags result to see how many bags will fit on the 
#    shelving unit.

import itertools

max_capacity = 1000
num_bags = 0

for i in itertools.count(start=13.5, step=13.5):
  if i >= max_capacity:
    break
  num_bags += 1

print(num_bags)

# Ok this was rough. I got the right formula and setup, i just didnt put the
# right start. I started from 0, when it should be from 13.5.
