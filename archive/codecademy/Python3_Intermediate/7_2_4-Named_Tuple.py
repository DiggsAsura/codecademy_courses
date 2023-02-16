# 7. Specialized Collections
# 2. Collections
# 4. Named Tuple

print('\nNamed Tuple\n---------------')

# Tuples, another common built-in container, are very useful for grouping
# together data that does not need to be modified in the future. Tuples do
# however run into an issue when they host various data and even nested data.
# Let's examine a tuple containing actor data:

actor_data_tuple = ('Leonardo DiCaprio', 1974, 'Titanic', 1997)

# In this example, we are storing details about an actor that is unlikely to 
# change (we can assume for now the actor's name will not change). While the
# tupple does a great job of creating a container that can keep ordered
# immutable data, it can become quite confusing to represent properties
# using numerical indices. For example:

actor_data_tuple[3]

# Unless we explicitly define a variable name that describes what the third
# index represents, it's very hard to tell what data we are talking about.
# We would also need to make separate variables for each property! Thanks to 
# the collections module, we have a solution to this problem.
#
# The namedtuple collection allows us to have an immutable tuple object, but
# every element becomes self-documented. Let's examine our actor example
# but now refactored to use a namedtuple:

from collections import namedtuple

#* General Structure:
#* namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

ActorData = namedtuple('ActorData', ['name', 'birth_year', 'movie', 'movie_release_year'])

# In this example, we are defining an instance of the namedtuple collection
# with a typename called 'ActorData' and a sequence of strings called
# field_names that represents the labels for the data we want to store.
#
# We are saying we want our namedtuple to be called 'ActorData' and for it to
# have name, birth_year, movie and movie_release_date properties. It's like
# creating a label system for the type of data inside of the tuple!
#
# We can then define an instance of our ActorData:

actor_data = ActorData('Leonardo DiCaprio', 1974, 'Titanic', 1997)

# This will then allow us to access the mapped property value to it's associated
# name from before using the . notation:

print(actor_data.name)

# Some things to note about namedtuples:
#
#   - You may have noticed we use a CapWords convention when defining our
#     namedtuple. This is because namedtuple actually returns a subclass and 
#     thus falls under the conventions we use for classes.
#
#   - The field_names argument can alternatively be a single string with
#     each fieldname separated by whitespace and/or commas, for example,
#     'x y', or 'x, y'.
#
#   - At first glance, namedtuples might seem like it is trying to replicate a
#     dictionary. While the key idea of labeling properties is the same in
#     both structures, namedtuples have some key advantages over a regular
#     dictionary:
#
#       - They are immutable and maintain their order, while a dictionary 
#         does not.
#
#       - They are more lightweight than dictionaries and take no more memory
#         than a regular tuple.
#
# There are other useful methods that a namedtuple uses such as converting
# from a namedtuple to a dict, replacing elements and filed names, and even
# setting default values for attributes. More information about namedtuple
# containers can be found in the Python Documentation:
# https://docs.python.org/3/library/collections.html#collections.namedtuple
#
# Let's now practice using the namedtuple container!


print('\nTasks\n------------')

# 1. We want to continue building out our clothing store application. We want
#    a standardized way to store clothing type, color, size, and price. To do
#    this, we can use a namedtuple!
#
#    Import the container and create a namedtuple subclass called ClothingItem
#    with a typename of 'ClothingItem' and the field_name consisting of:
#    'type', 'color', 'size', and 'price' in that specific order.
#
# 2. Let's test out our new ClothingItem namedtuple subclass!
#
#    For this checkpoint, create a new object from the subclass ClothingItem
#    called new_coat.
#
#    The new_coat should have a type of 'coat', a color of 'black', a size of
#    'small' and a price of 14.99.
#
# 3. Now that the new_coat object has been created, access the price of this 
#    namedtuple object and store it in a variable called coat_cost.
#
# 4. There is too much manual work when creating the namedtuple objects on at 
#    a time, so lets use a loop!
#
#    We have a list of tuples containing clothing information called clothes.
#
#    First, create a new empty list called updated_clothes_data and then for
#    every piece of clothes data in the list of tuples, append a new 
#    ClothingItem object to update_clothes_data while passing the data from
#    the tuple into the new ClothingItem object.
#
#    Print out updated_clothes_data to see the result!

clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'grey', 'small', 8.99)]

#from collections import namedtuple

ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)
coat_price = new_coat.price
print(new_coat)
print(coat_price)

updated_clothes_data = []
for item in clothes:
  updated_clothes_data.append(ClothingItem(item[0], item[1], item[2], item[3]))

for item in updated_clothes_data:
  print(item)
