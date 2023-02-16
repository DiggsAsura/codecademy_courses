# Chapter 11 - Classes
# 1. Introduction to Classes
# 1. Types

# Types
# Python equips us with many different ways to store data. A float is a different 
# kind of number from an int, and we store different data in a list than we do 
# in a dict. These are known as different types. We can check the type of a Python
# variable using the type() function:
#a_string = "Cool String"
#an_int = 12
#a_dict = {'cool': 'dict'}
#print(type(a_string))
#print(type(an_int))
#print(type(a_dict))
#
# Above, we defined two variables (well three, since I added one though lol), and 
# checked the type of these two variables. A variable's type determines what you can 
# do with it and how you can use it. You can't .get() something from an integer, 
# just as you can't add two dictionaries together using +. This is because those 
# operations are defined at the type level. 

# Tasks
# 1. Call type() on the integer 5 and print the result
# 2. Define a dictionary my_dict
# 3. Print out the type() of my_dict
# 4. Define a list called my_list
# 5. Print out the type() of my_list

print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))

