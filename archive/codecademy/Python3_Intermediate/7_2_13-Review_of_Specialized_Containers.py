# 7. Specialized Collections
# 2. Collections
# 13. Review of Specialized Containers

print('\nReview of Specialized Containers\n--------------------------')

# Nice work! We have learned about all sorts of advanced containers which can
# help make programming easier, more organized, and more optimized! We even
# learned how to make our own advanced containers using container wrappers.
# Let's review the use case for each of the advanced containers from
# the collections class:
#
#* deque
#   - An advanced container which is optimized for appending and popping items 
#     from the front and back. For accessing many elements positioned elsewhere,
#     it is better to use a list.
#
#* namedtuple
#   - The namedtuple lets us create an immutable data structure similar to a 
#     tuple, but we don't have to access the stored data using indices. Instead,
#     we can create instances of our namedtuple with named attributes. We can
#     then use the . operator to retrieve data by the attribute names.
#
#* Counter
#   - This advanced container automatically counts the data within a hashable
#     object which we pass into it's counstructor. It stores it as a dictionary
#     where the keys are the elements and the values are the number of 
#     occurences. 
#
#* defaultdict
#   - An advanced container which behaves like a regular dictionary, except that
#     it does not throw an error when trying to access a key which does not
#     exist. Instead, it creates a new key:value pair where the value defaults to
#     what we provide in the constructor for the defaultdict.
#
#* OrderedDict
#   - The OrderedDict combines the functionality of a list and a dict by preserving
#     the order of elements, but also allowing us to access values using keys
#     without having to provide an index for the position of stored dictionaries.
#
#* ChainMap
#   - This interesting container combines multiple mappings into a single
#     container. When accessing a value using a key, it will search through
#     every mapping contained within until a match is found or the end is reached.
#     It also provides some useful methods fro grouping parent and child
#     mappings.
#
#* UserDict
#   - This is a container wrapper which lets us create our own version of a
#     dictionary.
#
#* UserList
#   - This is a container wrapper which lets us create our own version of a 
#     list.
#
#* UserString
#   - This is a container wrapper which lets us create our own version of a 
#     string.
#
# Let's try combining some of these concepts by adding one last addition to 
# our clothes store app!


print('\nTasks\n------------')

# 1. The final addition to our clothes store app will be some logic for bundling
#    overstocked items into groups to sell at once. We would like to split our
#    items by price and then pick three cheaper items and two more expensive items
#    per bundle. Finally, we are going to promote the bundles which have a value
#    greater than 100 dollars.
#
#    For the first step, import the deque and namedtuple classes from the collections
#    module and create a new deque called split_prices.
#
# 2. Now that the deque has been created, for every clothes item in the 
#    overstock_items list, if the price is greater than 20 dollars, then append 
#    the item to the front of split_prices, otherwise append it to the back of
#    split_prices.
#
# 3. To make the data easier to read and work with, create a namedtuple subclass
#    called ClothesBundle. Set the typename to ClothesBundle and the field_names
#    to bundle_items and bundle_price.
#
# 4. This next step is a bit tricky. First, create an empty list called bundles.
#    Use a loop to continue iterating as long as there are at least 5 elements 
#    left in split_prices.
#
#    On each iteration, append a new ClothesBundle object to the bundles list.
#    The ClothesBundle object will be created by making a bundle of three cheap
#    items and two expensive items. This can be accomplished using list of items
#    by popping from the back of split_prices three times and popping from the
#    front of split_prices two times. 
#
#    Use that list of clothes items as the bundle_items in the ClothesBundle.
#    Calculate the sum of the prices for the bundle and store that as the 
#    bundle_price in the ClothesBundle.
#
# 5. Use the bundles list to find out which bundles should be promoted. Create
#    a new list called promoted_bundles. For every bundle in bundles which has
#    a total value of over 100 dollars, add that bundle to promoted_bundles.
#
# 6. Finally, print out the list of promoted_bundles to see the result!

overstock_items = [['shirt_103985', 15.99],
                    ['pants_906841', 19.99],
                    ['pants_765321', 15.99],
                    ['shoes_948059', 29.99],
                    ['shoes_356864', 9.99],
                    ['shirt_865327', 10.99],
                    ['shorts_086853', 9.99],
                    ['pants_267953', 21.99],
                    ['dress_976264', 32.99],
                    ['shoes_135786', 17.99],
                    ['skirt_196543', 12.99],
                    ['jacket_976535', 26.99],
                    ['pants_086367', 30.99],
                    ['dress_357896', 29.99],
                    ['shoes_157895', 14.99]]


# Checkpoint 1
from collections import deque, namedtuple

split_prices = deque()

# Checkpoint 2
for item in overstock_items:
  if item[1] > 20:
    split_prices.appendleft(item)
  else:
    split_prices.append(item)


# Checkpoint 3
ClothesBundle = namedtuple('ClothesBundle', ['bundle_items', 'bundle_price'])

# Checkpoint 4
bundles = []

while len(split_prices) >= 5:
  bundle_list = [split_prices.pop(), split_prices.pop(), split_prices.pop(),
   split_prices.popleft(), split_prices.popleft()]
  calc_price = sum(b[1] for b in bundle_list)
  bundles.append(ClothesBundle(bundle_list, calc_price))

promoted_bundles = []

for bundle in bundles:
  if bundle.bundle_price > 100:
    promoted_bundles.append(bundle)

print(promoted_bundles)  