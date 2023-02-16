# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 11. Review

# Good Job! In this lesson we covered:
#
#   - Iterables and iterators and how they differ.
#
#   - Using the iter() function to create an iterator.
#
#   - Using the next() function to manually iterate over an iterator
#
#   - How for loops use iterables and iterators
#
#   - How to write custom iterators by implementing the __iter__() and
#     __next__() methods.
#
#   - How to use built-in itertools including count(), chain() and
#     combinations().
#
# There is much more to discorver about iterators, iterables and itertools!
# Click the respective links to read more.
#
# https://docs.python.org/3/glossary.html#term-iterator
# https://docs.python.org/3/glossary.html#term-iterable
# https://docs.python.org/3/library/itertools.html?highlight=itertools
# 
# Let's practice these concepts some more!

###
# Tasks
########
#
# 1. Create a list iterable that contains tuples of (cat_toy, price). The
#    list should be called cat_toys. The tuple should consist of the cat toy
#    name and price following the values in the table:
#
#?   Toy            Price
#?   laser          1.99
#?   fountain       5.99
#?   scratcher      10.99
#?   catnip         15.99
#
# 2. Using iter(), create an iterator called cat_toy_iterator that retrieves
#    the iterator for cat_toys.
#
# 3. Using four next() statements, print out each value in cat_toy_iterator.
#
# 4. A customer enters an only has $15 to spend on exactly 2 cat toys. They
#    want to know how many combinations of the available toys they can
#    afford, while only getting 2 of them total.
#
#    First, import itertools at the top of the module.
#
# 5. Next, above the commented out for loop, create a combinations() iterator
#    called toy_combos to retrieve all combinations of 2 total toys from the
#    cat_toys list.
#
# 6. Uncomment all lines of the for loop.
#
#    Each iteration of the for loop gives a tuple that is within toy_combos.
#    The variable toy1 represents index 0 of the tuple (the toy name) and
#    cost_of_toy1 represents index 1 of the tuple (the toy cost).
#    We repeat this to store the toy name and price of toy 2 via variables toy2
#    and cost_of_toy2
#
#    After the final line within the for loop, check if the price of cost_of_toy1
#    and cost_of_toy2 is less than or equal to max_money which is the
#    $15 the customer has to spend. If it is, add the tuple to the options list.
#
# 7. Print the final options list to see what toy combinations the customer
#    can buy with $15.
#
######

import itertools

max_money = 15
options = []

cat_toys = [('laser', 1.99), ('fountain', 5.99), 
            ('scratcher', 10.99), ('catnip', 15.99)]

cat_toy_iterator = iter(cat_toys)
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator)) 

toy_combos = itertools.combinations(cat_toys, 2)

for combo in toy_combos:
  toy1 = combo[0]
  cost_of_toy1 = toy1[1]
  toy2 = combo[1]
  cost_of_toy2 = toy2[1]
  
  if (cost_of_toy1 + cost_of_toy2) <= max_money:
    options.append((toy1, toy2))

for combo in options:
  print(combo)
    
