# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Function Arguments
# 1. Function Arguments: A Recap

# In Python, there are three common types of function arguments: 
#
#   - Positional arguments: arguments that are called by their position
#     in the function definition
#
#   - Keyword arguments: arguments that are called by their name
#
#   - Default arguments: arguments that are given default values.
#
# To recap, here is what each of these arguments looks like:
#
# Positional:
#def print_name(first_name, last_name):
#  print(first_name, last_name)
#print_name('Jiho', 'Baggins')
#
# Here, first_name will be mapped to 'Jiho' while last_name will be mapped
# to 'Baggins' due to the position of the arguments when calling the 
# function.
#
#
# Keyword Arguments
#def print_name2(first_name, last_name):
#  print(first_name, last_name)
#print_name2(last_name='Baggins', first_name='Jiho')
#
# Here, we are using the parameter names first_name and last_name as keyword
# arguments in the function call. Notice the order of the arguments does
# not matter since they are assigned to a specific name. 
#
#
# Default arguments
#def print_name3(first_name='Jiho', last_name='Baggins'):
#  print(first_name, last_name)
#print_name3()
#
# Here, in the function definition, we assign default values to the
# parameters. This means we can call our function without providing any
# arguments because they will have a value to fall back onto.

# While these are the most common argument types, in this lesson, we will
# explore what happens when we want to make our function arguments more
# flexible by taking a varying number of arguments. 
#
# Before we jump into learning more about variable argument types, let's 
# review the most common types to get warmed up. 

# Tasks
# 1. Examine the dictionary and run the code to move on.. 
# 2. Create a function add_table which update the dictionary
# 3. Add customer with positional arguments and print a new customer
# 4. Add customer with keyword arguments
# 5. Modify the function definition of assign_table to have default vip_status value False
# 6. Add 4, Sarah. She's not VIP so should not have to edit that argument.

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: []
}
#print(tables)

def assign_table(table_number, name, vip_status=False):
  return tables.update({table_number: [name, vip_status]})

assign_table(2, 'kenneth', True)
#print(tables)

assign_table(vip_status="True", table_number=3, name="Ka Yi")
#print(tables)

assign_table(4, 'Sarah')
print(tables)