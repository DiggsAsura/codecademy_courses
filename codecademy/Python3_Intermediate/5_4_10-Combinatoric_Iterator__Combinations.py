# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 10. Combinatoric Iterator: Combinations

# A combinatoric iterator will perform a set of statistical or mathematical
# operations on an input iterable.
#
# A useful itertool that is a combinatoric iterator is the combinations() 
# itertool. This itertool will produce an iterator of tuples that contain
# combinations of all elements in the input.

#! combinations(iterable, r)

# The combinations() itertool takes in two inputs, the first is an iterable,
# and the second is a value r that represents the length of each combination
# tuple.
#
# The return type of combinations() is an iterator that can be used in a for
# loop or can be converted into an iterable type using list() or a set().
#
# To show how it's used, suppose we have a list of even numbers and we want
# all possible combinations of 2 even 2 numbers:

#!import itertools
#!
#!even = [2, 4, 6]
#!even_combinations = list(itertools.combinations(even, 2))
#!print(even_combinations)

# Here we:
#
#   - Import the module itertools.
#
#   - Create an iterator using combinations() with the list of even numbers 
#     as the first argument and 2 as the second argument.
#
#   - Set even_combinations equal to a list of the elemtns in the iterator
#     returned from combinations()
#
#   - Print even_combinations. The resulting list of 2 member tuples
#     are the combinations of all 3 members of even:
#
#!    [(2, 4), (2, 6), (4, 6)]
#
# Now, let's try using a combinations itertool within our pet store!

###
# Tasks
#########
#
# 1. We have another shelving unit to display by the register that can only
#    hold 3 collars. We have a list of collars of varying colors and sizes.
#
#    We want to know how many different combinations exist to display a set
#    of 3 collars. Use the combinations() itertool to do this. Set the 
#    returned iterator to a variable named collar_combo_iterator
#
# 2. Using a for loop, print each item in collar_combo_iterator to see all 
#    the possible collar combinations.
#
####

import itertools

collars = ["Red-S", "Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

#collar_combo_iterator = list(itertools.combinations(collars, 3))
collar_combo_iterator = itertools.combinations(collars, 3) 

for combo in collar_combo_iterator:
  print(combo)
