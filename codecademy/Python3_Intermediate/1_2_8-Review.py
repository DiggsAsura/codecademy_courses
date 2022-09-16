# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Function Arguments
# 8. Review

# We covered a lot of ground in this lesson! We learned all about how 
# functions can accept different arguments and different syles in which
# we can pass those arguments in. We learned:
#
# - How to pack positional arguments in a function with *args
# 
# - How to work with *args using iteration and other positional arguments.
# 
# - How to pack keyword arguments in a function with **kvargs
#
# - How to work with **kwargs using iteration and other keyword arguments.
#
# - How to combine all different types of arguments to gain the most
#   flxibility in our function declarations
#
# - How to use an unpacking operator (* or **) to unpack arguments in 
#   a function call. 
# 
# - How to use unpacking operator (* or **) on iterables.
#
# We should now be able to read many different styles of function writing in
# Python and come up with ways to call those functions with style and 
# clarity. 

# Take some time to examine the application we built for Jiho. The program
# has been adjusted to account for the payment calculation from the
# previous step!
#
# Play around and have fun with our new knowledge of function arguments. 
# Here is some additional functionality that Jiho might like:
#
# - The ability to remove a table's guests when they leave the resturant
#
# - An adjustment to the calculate_price_per_person() function
#   to access a tables 'total' and return the result. 
#
# - The ability to add and remove order items for both food and drinks
#   if there is ever a mistake
#
# - The ability to queue reservations for later times for specific tables


tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
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
  
def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks
  
def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)
  

calculate_price_per_person(1000, 200, 5)