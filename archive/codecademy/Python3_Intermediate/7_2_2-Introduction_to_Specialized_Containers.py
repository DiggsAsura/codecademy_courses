# 7. Specialized Collections
# 2. Collections
# 2. Introduction to Specialized Containers

print('\nIntroduction to Specialized Containers')

# Now that we've had a refresher on some of the built-in containers Python
# provides, let's dive into the collections module.
#
# The classes from the collections module are very similar to the built-in 
# containers we've been already using, but they contain new methods and utilities.
# Each of these specialized containers focuses on a certain improvement to its
# built-in counterpart such as optimizing performance, better organization, 
# fewer steps for performing tasks, and more!
#
# In order to use classes from the collections module, we will first need to
# import the module into our code. This is different than the previous
# containers we've seen because they were built-in and did not require an 
# import.
#
# Here are some of the various ways importing will look like:

#* To import a single class or multiple classes
#from collections import namedtuple, deque

#* To import all classes in the collections module
#from collections import *

#* Another way to import all classes in a module
#import collections

# For a more specific example, here is what importing the OrderedDict (one of
# the specialized containers) would look like. We will dive deeper into the
# details of this particular container later on it this lesson but for now
# just observe the syntax:


#from collections import OrderedDict
#orders = OrderedDict({
#  'order_4829': {
#    'type': 't-shirt',
#    'size': 'large',
#    'price': 9.99
#  },
#  'order_6184': {
#    'type': 'pants',
#    'size': 'medium',
#    'price': 14.99
#  },
#  'order_2905': {
#    'type': 'shoes',
#    'size': 12,
#    'price': 22.50
#  }
#})
#
#orders.move_to_end('order_4829')
#orders.popitem()


# You might have noticed that this is a similar example to the dictionary review
# in the last exercise, but there are some new methods that provide even more
# functionality to the traditional dictionary.
#
# Here is a list of all of the advanced containers we will be looking at in 
# this lesson:
#
#   - deque
#   - namedtuple
#   - defaultdict
#   - OrderedDict
#   - ChainMap
#
# Container Wrappers:
#
#   - UserDict
#   - UserList
#   - UserString
#
# Play around with the provided specialized OrderedDict collection. Click Next
# to move on!

from collections import OrderedDict

orders = OrderedDict({
  'order_4829': {
    'type': 't-shirt', 
    'size': 'large', 
    'price': 9.99
    },
  'order_6184': {
    'type': 'pants', 
    'size': 'medium', 
    'price': 14.99
    },
  'order_2905': {
    'type': 'shoes', 
    'size': 12, 
    'price': 22.50
    }
  })

orders.move_to_end('order_4829')
orders.popitem()
print(orders)