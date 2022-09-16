# 7. Specialized Collections
# 2. Collections
# 6. OrderedDict

print('\nOrderedDict\n----------------')

# When keeping track of many different dictionaries with the built-in Python
# containers, we could try storing dictionaries in a list, or even a dictionary
# of dictionaries. This may work in some cases, but there are a few problems
# which might come up.
#
# When storing dictionaries in a list, the order is preserved, but we have to
# access the elements by their index before we can access the dictionary:

first_order = {
  'order_2905': {
    'type': 'shoes',
    'size': '12',
    'price': 22.50
  },
}
second_order = {
  'order_6184': {
    'type': 'pants',
    'size': 'medium',
    'price': 14.99
  },
}
third_order = {
  'order_4829': {
    'type': 't-shirt',
    'size': 'large',
    'price': 9.99
  }
}

list_of_dicts = [first_order, second_order, third_order]

# In order to get the price of a specific order, we must know the index of it 
# already before we can access the dictionary data stored inside:

print(list_of_dicts[1]['order_6184']['price'])

# On the other hand, depending on the Python version, the dict container can
# preserve the order, but it is difficult to move elements around:

dict_of_dicts = {}
dict_of_dicts.update(first_order)
dict_of_dicts.update(second_order)
dict_of_dicts.update(third_order)

print(dict_of_dicts['order_6184']['price'])

# Note: The dict class is unordered in earlier versions of python, so implementing
# it this way must have version 3.6 or greater.
#
# To solve these issues, we can use an OrderedDict!
#
# The OrderedDict container allows us to access values using keys, but it also 
# preserves the order of the elements inside of it. Let's take a closer look at
# the example of processing customer orders from earlier in the lesson:
#
# Import and create OrderedDict:
from collections import OrderedDict
orders = OrderedDict()

# The order of data is preserved when adding it to the OrderedDict:
orders.update({
  'order_2905': {
    'type': 'shoes',
    'size': 12,
    'price': 22.50
  }})
orders.update({
  'order_6184': {
    'type': 'pants',
    'size': 'medium',
    'price': 14.99
  }})
orders.update({
  'order_4829': {
    'type': 't-shirt',
    'size': 'large',
    'price': 9.99
  }})

# Data can be accessed using keys like a normal dictionary:
find_order = orders['order_2905']

# The order can be retrieved by converting it to a list then accessing by 
# index:
orders_list = list(orders.items())
third_order = orders_list[2]
print(third_order)

# When using an OrderedDict, we are able to use its methods for moving the
# data around. We can move an element to the back or front and pop the data
# from the back or front of the OrderedDict:
orders.move_to_end('order_4829')

# Pop the last item in the dictionary
last_order = orders.popitem()
print(f'{last_order} << ')

# Note: These two methods also accept boolean arguments which determine if the
# element is moved / popped from the front or back of the OrderedDict.
#
# For more information about the OrderedDict container, take a look at the
# Python Documentation https://docs.python.org/3/library/collections.html#collections.OrderedDict
#
# Now let's try using an OrderedDict in our clothes app!


print('\nTasks\n-----------')

# 1. We want to add some logic to our application which will organize orders by
#    their status. The status of an order can be purchased, returned, or 
#    canceled. To make things more organized, we want to remove the canceled
#    orders and push the returned orders to the end. In order to do this, we can
#    use an OrderedDict !
#
#    For this first checkpoint, import the OrderedDict class and create a new 
#    object from that class called orders. Use the constructor to automatically
#    convert the ordered_data into an OrderedDict.
#
# 2. We need to keep track of which orders to remove and which ones to push back.
#    To do this, create two new lists called to_move and to_remove. Iterate through
#    each item in orders and check what the status is. If the status is 
#    'returned' then add the key (order number string) to the to_move list.
#    Otherwise, if the status is 'canceled' then add it to the to_remove list.
#
# 3. Now that we have the list of items to remove from orders, for every item
#    in the to_remove list, .pop() the elements from orders.
#
# 4. Now that all of the canceled orders have been removed, use another loop to 
#    push back any of the 'returned' orders from to_move to the end of orders.
#    This will be similar to the last step, but this time we are using the
#    .move_to_end() method.
#
# 5. Finally, use print to output the orders to the console!

#from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

orders = OrderedDict(order_data)

to_move = []
to_remove = []

for order, status in orders.items():
  if status == 'returned':
    to_move.append(order)
  elif status == 'canceled':
    to_remove.append(order)

print(to_move)    
print(to_remove)

for order in to_remove:
  orders.pop(order)

for order in to_move:
  orders.move_to_end(order)

for order, status in orders.items():
  print(f'{order} \n\tStatus: {status}')