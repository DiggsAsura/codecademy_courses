# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Function Arguments
# 5. Working with **kwargs

# Working with **kwargs looks very similar to its *args counterpart. Since ** generates a 
# standard dictionary, we can use iteration just like we did earlier by taking advantage of the
# .values() method. Here is an example
#def print_data(**data):
#  for arg in data.values():
#    print(arg)

#print_data(a='arg1', b=True, c=100)
#
# Would output
# arg1
# True
# 100
#
# We can also combine our use of ** with regular positional arguments. However, Python requires
# that all positional arguments come first in our function definition. Let's examine how this works:
#def print_data2(positional_arg, **data):
#  print(positional_arg)
#  for arg in data.values():
#    print(arg)

#print_data2('position 1', a='arg1', b=True, c=100)
#
# Would output
# position 1
# arg1
# True
# 100
#
# If we were to switch the position of positional_arg to come after **data, we would be met with
# a SyntaxError. 
#
# Let's expand our resturant application from the previous exercises to apply the flexibility of 
# using **kwargs in our functions.

# Tasks
# 1. In the last exercise, we saw how using ** allowed us to capture different food items that
#    a table will order. In the next few checkpoints, we will finish implementing the functionality
#    of our assign_food_items() function.
#
#    Take some time to get reacquainted with the program. Note the changes in the 
#    assign_food_items() funciton.
#
#    Run the code to move on!
#
# 2. Unfortunately, when we orginally implemented assign_food_items we did not assign the values we
#    capture into our tables dictionary.
#
#    Adjust the function definition of assign_food_items():
#
#     - Add a positional parameter called table_number followed by the **order_items parameter
#       we already defined. 
#
#     - Uncomment the 2 lines inside the function.
#
#    Adding the parameter and uncommenting the lines will now allow us to assign food to a 
#    specific table.
#
# 3. Great! Now that we have the base functionality set up, let's give it a test run. 
#    Luckily a new customer named Douglas just came in and is ready to place an order.
# 
#    Under print('\n --- tables after update --- \n'), call the assign_food_items() 
#    function with the following arguments:
#
#      - A positional argument table_number with the value of 2
#      - A keyword argument food with the value 'Seabass, Gnocchi, Pizza'
#      - A keyword argument drinks with the value 'Margarita, Water'
#
#    Print tables to see the change!

tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancaces'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {}
}

def assign_table(table_number, name, vip_status=False):
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks


print('\n --- tables after update --- \n')

assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')

print(tables)

# This is kinda overwhelming. Working with tuples and dictionaries is kinda alien still. While
# I do understand it somewhat when reading, I'm more afraid if it will stick anytime soon, and 
# make sense for own projects. 

# Oh well - got most of them right though :) Next!