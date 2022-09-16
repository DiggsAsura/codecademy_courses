# 7. Specialized Collections
# 2. Collections
# 8. Counter

print('\nCounter\n-------------')

# One of the most common tasks we might have to do in a program is to count
# instances of an element in a collection. Below, we will examine a Python
# list and look at one particular way we count elements, and then see how
# the collections module allows us to improve upon our implementation using the
# Counter collection.
#
# First, let's define a list of items. Since we have been working on an application
# for our clothing store, lets stick with clothing items:

clothes_list = ['skirt', 'hoodie', 'dress', 'blouse', 'jeans', 'shoes', 'skirt', 'skirt', 'jeans', 'hoodie', 'boots', 'jeans', 'jacket', 't-shirt', 'skirt', 'skirt', 'dress', 'shoes', 'blouse', 'hoodie', 'skirt', 'boots', 'shoes', 'boots', 'jeans', 'hoodie', 'blouse', 'hoodie', 'shoes', 'shoes', 'blouse', 'boots', 'blouse', 'hoodie', 't-shirt', 'jeans', 'dress', 'skirt', 'jacket', 'boots', 'skirt', 'dress', 'jeans', 'jeans', 'jacket', 'jeans', 'shoes', 'dress', 'hoodie', 'blouse']

# If we wanted to create a representation of how many of each item exist in our
# collection, we could use a loop and a dictionary. Here is what it might 
# look like:

counted_items = {}
for item in clothes_list:
  if item not in counted_items:
    counted_items[item] = 1
  else:
    counted_items[item] += 1

print(counted_items)

# This would output 
# {'skirt': 8, 'hoodie': 7, 'dress': 5, 'blouse': 6, 'jeans': 8, 'shoes': 6, 'boots': 5, 'jacket': 3, 't-shirt': 2}

# While this is a perfectly sound solution to our counting problem, we can actually
# accomplish this goal much quicker using the Counter container!
#
# The Counter container instantly counts elements for any hashable object. It
# stores the data as a dictionary where the keys are the elements and the values are
# the number of occurrences. Here is what the same problem looks like, but with
# the Counter container:

from collections import Counter

counted_items = Counter(clothes_list)
print(counted_items)

# Would output:
# Counter({'skirt': 8, 'jeans': 8, 'hoodie': 7, 'blouse': 6, 'shoes': 6, 'dress': 5, 'boots': 5, 'jacket': 3, 't-shirt': 2})

# This allows us to create a much more elegant solution without many lines of
# code. Additionally, the Counter class has methods that provide further utility
# when working with our data. These methods include mathematical operations for 
# subtracting one count dictionary from another, finding the most common elements,
# and even generating a new list of elements based on the number of occurences.
#
# For more information about the Counter class, take a look at the Python
# documentation: https://docs.python.org/3/library/collections.html#collections.Counter
#
# Let's now practice using the Counter class!


print('\nTasks\n-------------')

# 1. We have decided to add some more logic to our clothing store application
#    to automatically calculate how much of each product has been sold based on
#    our inventory at the start of the day vs the end of the day.
#
#    First, let's define a function called find_amount_sold. Our function
#    will need three parameters: opening, closing and item. For now, inside
#    of the function, simply add the keyword return. Also, don't forget to
#    import the Counter class as we will be using it throughout the checkpoints.
#
# 2. At this point, we could create two loops to meticulously count every item 
#    in each list, but instead, let's create two Counter objects to calculate
#    a count of items in our opening and closing inventory.
#
#    Inside of our new function, and before it returns, create a variable
#    called opening_count and store a Counter object passing in the opening
#    parameter as the counter's input.
#
#    Then, create a variable called closing_count which stores a Counter object
#    and passes in the closing parameter into the Counter.
#
# 3. Next, we'll have to subtract the closing counted data from the opening
#    counted data in order to get the amount sold for every item. Luckily,
#    the Counter container has a method that allows us to accomplish this 
#    really easily.
#
#    Take a look at the Python documentation for the .subtract() method.
#    https://docs.python.org/3/library/collections.html#collections.Counter.subtract
#
#    When you are ready, call the .subtract() method on opening_count and pass
#    in closing_count as the first argument.
#
# 4. Awesome! Now we have our Counter object with the difference in item 
#    inventory. You may have noticed earlier we defined a parameter named item
#    in our function declaration. This is because the goal of our function is
#    to return the difference in inventory for a specific item rather than all
#    of them!
#
#    Using the parameter item, access the item's inventory from the opening_count
#    Counter object and return it.
#
# 5. Finally, let's test out our function by calling it with opening_inventory as 
#    the first argument, closing_inventory as the second argument, and t-shirt
#    as the third argument.
#
#    Store the result in a variable called tshirts_sold and then use print()
#    to display it!

#!from collections import Counter

opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']
closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']


def find_amount_sold(opening, closing, item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)
  opening_count.subtract(closing_count)
  return opening_count[item]

print(find_amount_sold(opening_inventory, closing_inventory, 'shoes'))

# Don't fully understand the return of the function. 