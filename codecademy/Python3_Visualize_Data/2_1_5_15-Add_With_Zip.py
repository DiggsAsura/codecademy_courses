# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 15. Add With Zip

'''
In the following exercises, you will be given two lists and asked to perform
operations of corresponding elements of these lists. This can be done by using
List Comprehension and the built-in Python function zip. Take a look at the
documentation for zip.
https://docs.python.org/3/library/functions.html#zip


a = [1, 2, 3]
b = [4, 5, 6]
combined = zip(a, b)

In the code above, combined now contains

[(1, 4), (2, 5), (3, 6)]

We can now use List Comprehension to iterate through this list to create 
something new!
'''

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

sums = [num1 + num2 for (num1, num2) in zip(a, b)]
print(sums)