# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 18. Ages

''' 
To concatenate a string and an integer, we need to first use the str() function
to cast the integer to a string. When you pass in a number to str(), it is 
returned to you as a string:

str(10)
"10"

str(0)
"0"

str(222)
"222"

After you have cast an integer to a string, you can concatenate it to another
string by using +: 

"I have " + str(100) + " cats!"


...or just fuck that since i use f'' ;-)
'''

names = ['Shila', 'Arya', 'Kele']
ages = [14, 9, 35]

print([f'Name: {name}, Age: {age}' for (name, age) in zip(names, ages)])
