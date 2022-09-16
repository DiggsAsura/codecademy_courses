# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 10. Same String

'''
String comparison can be done using ==

"Hello" == "Hello!"
False

"Hi" == "Hi"
True

"Hello" == ""
False
'''

names = ['Elaine', 'George', 'Jerry', 'Cosmo']

is_Jerry = [name == 'Jerry' for name in names]
print(is_Jerry)