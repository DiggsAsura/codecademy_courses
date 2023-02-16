# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 7. First Character

''' 
You can get a character of a string by using the syntax [index], where index
is the character you want to get, starting at 0.

For example:

my_string = "Whoa! A seesaw"
print(my_string[0])
print(my_string[2])
print(my_string[5])

"W"
"o"
" "

'''

names = ['Elaine', 'George', 'Jerry', 'Cosmo']
print([name[0] for name in names])