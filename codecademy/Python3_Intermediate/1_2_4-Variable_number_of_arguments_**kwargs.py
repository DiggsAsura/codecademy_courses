# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Function Arguments
# 4. Variable number of arguments: **kwargs

# Python doesn't stop at allowing us to accept unlimited positional arguments; it also gives
# us the power to define functions with unlimited keyword arguments. The syntax is very similar
# but uses two asterisks ** instead of one. We typically call these kwargs as a shorthand for
# keyword arguments.
#
# Let's examine a function that prints out some useful information about kwargs to see it 
# in action:
#def arbitrary_keyword_args(**kwargs):
#  print(type(kwargs))
#  print(kwargs)
  # See if there's an 'anything_goes' keyword arg and print it
#  print(kwargs.get('anything_goes'))
#
#arbitrary_keyword_args(this_arg="wowzers", anything_goes=101)
#
# Would output:
# <class 'dict'>
# {'this_arg': 'wowzers', 'anything_goes': 101}
# 101
#
# We can observe two things:
#   - **kwargs take the form of a dictionary with all the keyword argument values passed to 
#     arbitary_keyword_args. Since **kwargs is a dictionary, we can use standard dictionary 
#     functions like .get() to retrieve values.
#
#   - Just as we saw with *args, the name of kwargs is completely arbitrary, and this example 
#     works exactly the same with the name becoming data:
#     def arbitrary_keyword_args(**data):
# 
# Let's practice using **kwargs to get a feel of how it works in a function!

# Tasks
# 1. Jiho is pleased with how we can store orders for our tables. However, the staff now wants 
#    to distinguish between food items and drinks. 
#
#    Since food items get prepared in the kitchen and the drinks are prepared at the bar, it's 
#    important to distinguish between the two in our application.
#
#    The tables dictionary has been changed to support the staff's requests. Take some time to 
#    examine the changed structure. 
#
#    Run the code to move on to the next checkpoint!
#
# 2. Since our program now requires a distinction between food items and drinks, this is a great
#    place to utilize the power of **kwargs. 
#
#    Define a function called assign_food_items() that has one parameter, order_items. Pair 
#    this parameter with a ** operator to handle any keyword arguments. 
# 
#    For now, just have the function print order_items.
#
# 3. Now we want to capture the food items and drinks in order_items. Use the .get() method to do 
#    the following:
#
#     - Capture the values from a keyword argument called food and assign it to a 
#       variable called food
#     - Capture the values from a keyword argument called drinks and assign it to a variable 
#       called drinks
#
#    Refer to the commented example call at the bottom of the script for a reference on how 
#    we will call this function later on.
#
# 4. Lastly, inside of our function use print() to output the food variable and another print()
#    to output the drinks variable.
#
# 5. Uncomment the example call provided to test our function.

tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {}
}
#print(tables)


def assign_food_items(**order_items):
  #print(order_items)
  # Ok this part I needed the Hint, but not the solution :)
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  print(food)
  print(drinks)

assign_food_items(food='Pancakes, Poached Egg', drinks='Water')


# OK got it :) 