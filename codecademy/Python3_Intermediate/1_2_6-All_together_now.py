# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Function Arguments
# 6. All together now!

# So far we have seen how both *args and **kwargs can be combined with standard arguments. This is
# useful, but in some cases, we may want to use all three types together! Thankfully Python
# allows us to do so as long as we follow the correct order in our function definition. The order
# is as follows:
#
# 1. Standard positional arguments
# 2. *args
# 3. Standard keyword arguments
# 4. **kwargs
#
# As an example, this is what our function definition might look like if we wanted a function that
# printed animals utilizing all three types:
#def print_animals(animal1, animal2, *args, animal4, **kwargs):
#  print(animal1, animal2)
#  print(args)
#  print(animal4)
#  print(kwargs)
#
#print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='cat', animal5='Dog')
#
# The result would be:
# Snake Fish
# ('Guinea Pig', 'Owl')
# Cat
# {'animal5': 'Dog'}
#
# That is a whole lot of arguments! Let's break it down:
#
#   - The first two arguments that our function accepts will take the form of standard positional
#     arguments. When we call the function, the first two values provided will map to animal1
#     and animal2. Thus, the first line of output is Snake Fish
#   - The non-keyword arguments that follow after Snake and Fish in our function call are mapped 
#     to the args tuple. Thus, our result is ('Guinea Pig', 'Owl')
#   - Then we transition to regular keyword arguments. Since we called animal4 as a keyword, 
#     our result for the print statement is Cat
#   - Lastly, we have one more keyword argument that is mapped to **kwargs. Thus, our last line 
#     of output is {'animal_5': 'Dog'}
#

# Tasks
# 1. For an upcoming holiday, Jiho plans on making a prix fixe menu for the resturant. Customers at
#    the resturant will be able to choose the following:
#     - 1 Appetizer
#     - 2 Entrees
#     - 3 Side dish
#     - 2 Scoops of different ice cream flavors for dessert
#
#    To accomplish all these choices, we are going to utilize the different types of arguments that 
#    we have learned so far. Now that we've set up our goals, hit "Run" to move on to the next
#    step.
#
# 2. Let's start by defining a function called single_prix_fixe_order() which define four parameters
#    to accept the full order:
#     1. A parameter named appetizer
#     2. A parameter entrees paired with a * operator
#     3. A parameter named sides
#     4. A parameter named dessert_scoops paired with a ** operator
#
#    Our function should simply have four prin() statements that print each individual parameter.
#
# 3. We got our first prix fixe order in! The customer wants the following:
#     1. 'Baby Beets' as an appetizer
#     2. 'Salmon' and 'Scallops' as entrees
#     3. 'Mashed Potatoes' as side
#     4. A scoop of 'Vanilla' ice cream and a scoop of 'Cookies and Cream' for dessert
#
#    Utilize our function single_prix_ifxe_order() to print out all of the customer order.

def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
  print(appetizer)
  print(entrees)
  print(sides)
  print(dessert_scoops)

single_prix_fixe_order('Baby Beets', 'Salmon, Scallops', sides='Mahsed Potatoes', dessert_scoops='Vanilla, Cookies and Cream')

# OK nice, easy one. Got a couple of syntax errors, but fixed only based on those. 
# Mainly it was at first I didn't remember to address the different types of arguments (where
# keyword arguments and **kwargs will need argument= )