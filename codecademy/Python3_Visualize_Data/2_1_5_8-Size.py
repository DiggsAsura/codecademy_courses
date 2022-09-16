# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 8. Size

'''
To find the number of characters in a string, we use len. This block of code:

print(len("Hello"))
print(len("world"))
print(len("Hello, world!"))

5
6
13
'''

names = ['Elaine', 'George', 'Jerry', 'Cosmo']
print([len(name) for name in names])