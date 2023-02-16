# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 9. Opposite

'''
We can use the not operator to flip the value of a Boolean:

a = False
b = True

not_a = not a
not_b = not b

print(not_a)
print(not_b)

True
False
'''

booleans = [True, False, True]
opposite = [not boolean for boolean in booleans]

print(opposite)