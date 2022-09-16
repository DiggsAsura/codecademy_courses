# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 2. Squares

''' 
For this list comprehension, you will need to make use of range and number
squaring.

Range

The range(n) function gives you a list of numbers in order, starting from 0 and
going up to and not including n. For example:

range(5)

would yield

[0, 1, 2, 3, 4]


Squaring

You can find the square of a number by multiplying it by itself:

eight_squared = 8*8
# the value of eight_squared is now 64

or by using the exponential operator **:

seven_squared = 7**2
# the value of seven_squared is now 49
'''

nums = range(11)
squares = [num**2 for num in nums]
print(squares)