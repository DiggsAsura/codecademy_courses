# 7. Specialized Collections
# 2. Collections
# 3. Deque

print('\nDeque\n---------')

# In Python, lists are one of the most common containers we use to work with
# data. Unfortunately, there are certain situations where they perform poorly.
#
# Let's imagine a situation where we are processing a large document containing
# bug reports for an application. In order to prioritize the most important
# bugs, we want any normal bug reports to be appended to the end of the list and
# higher priority bugs to be at the front of the list (kind of like a priority
# list). As we fix the bugs, they can be removed from the front of the list.
#
# The program below is an example of what our implementation might look like
# using lists. Take some time to understand what the code is doing.

#!def get_all_bug_reports():
#!  pass

#!bug_data = []
#!loaded_bug_reports = get_all_bug_reports()

#!for bug in loaded_bug_reports:
#!  if bug['priority'] == 'high':
#!    bug_data.insert(0, bug)
#!  else:
#!    bug_data.append(bug)

#! A list must provide an index to pop
#!next_bug_to_fix = bug_data.pop(0)

# The problem with this implementation is that lists are not optimized for appending
# and popping large amounts of data, although they are great at accessing data at
# any index which you provide.
#
# To solve this problem, we can use dque containers. These are similar to lists,
# but they are optimized for appending and popping to the front and back, rather
# than having optimized accessing. Because of this, they are great for working 
# with data where you don't need to access elements in the middle very often or
# at all.
#
# Let's observe our sample program bug implemented with a deque:

#!from collections import deque

#!bug_data = deque()
#!loaded_bug_reports = get_all_bug_reports()

#!for bug in loaded_bug_reports:
#!  if bug['priority'] == 'high':
#!    bug_data.appendleft(bug)
#!  else:
#!    bug_data.append(bug)

#!next_bug_to_fix = bug_data.popleft()

# More information about deque container can be found in the Python
# Documentation: https://docs.python.org/3/library/collections.html#collections.deque
#
# Now let's try working with a larger amount of data where a deque is more
# beneficial!


print('\nTasks\n---------')

# 1. We need to order a large number of supplies for our clothing company. A CSV
#    file has been given to us by our team which lists each of the material's
#    names, the quantitiy, and the importance of the material.
#
#    A function is provided which reads the CSV file and returns a list of lists
#    containing the data in the format of [[material, number_of_pallets,
#    importance], [material, number_of_pallets, importance], ...].
#
#    We'll need to use a deque to separate the data into important and 
#    non-important items using our new trusy deque collection. First, create
#    an empty deque called supplies_deque.
#
# 2. Using a for loop, read each item from csv_data. On each iteration, if the
#    item is marked as important, append it to the front of supplies_deque, 
#    otherwise append it to the end.
#
# 3. Your accountant let you know that you have enough of a budget to order
#    25 important materials and 10 unimportant materials.
#
#    For this step, create a new deque called ordered_important_supplies.
#    Remove the 25 important items from your supplies_deque and append them
#    to ordered_important_supplies.
#
# 4. Now that you have completed the orders for the 25 important items, repeat
#    the same process for 10 unimportant items.
#
#    Create a new deque called ordered_unimportant_supplies. Remove 10 low 
#    important items from your supplies_deque and append them to
#    ordered_unimportant_supplies.

from helper_functions import process_csv_supplies
from collections import deque

# First line is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]


supplies_deque = deque()

for item in csv_data:
  if item[2] == 'important':
    supplies_deque.appendleft(item)
  else:
    supplies_deque.append(item)

ordered_important_supplies = deque()
ordered_unimportant_supplies = deque()

for i in range(25):
  ordered_important_supplies.append(supplies_deque.popleft())

for i in range(10):
  ordered_unimportant_supplies.append(supplies_deque.pop())

print(f'Important orders ({len(ordered_important_supplies)}):')
for row in ordered_important_supplies:
  print(row)

print(f'\nUnimportant orders ({len(ordered_unimportant_supplies)}):')
for row in ordered_unimportant_supplies:
  print(row)
