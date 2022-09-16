# 7. Specialized Collections
# 2. Collections
# 5. DefaultDict

print('\nDefaultDict\n------------')

# Dictionaries are another popular type of collection we use in our programs.
# Although they are great for a lot of situations, applications that rely
# heavily on them always run into a common issue. The issue deals with how to
# handle missing keys!
#
# When we try to access a key-value pair in a dictionary, but the key does not 
# exist, a dictionary will normally throw a KeyError. Take a look at this example
# of accessing an invalid key from a normal dictionary:

prices= {'jeans': 19.99, 'shoes': 24.99, 't-shirt': 9.99, 'blouse': 19.99}

#! KeyError: 'jacket'
#print(prices['jacket'])

# Dealing with frequent KeyError excaptions can be quite cumbersome and in 
# certain cases, it might be better to avoid throwing an error. One of the
# ways Python offers to deal with this issue is by having a default missing
# value in the dictionary, and this is exactly what the defaultdict collection
# does. Let's explore this new collection together!

from collections import defaultdict
validate_prices = defaultdict(lambda: 'No Price Assigned')

validate_prices['jeans'] = 19.99
validate_prices['shoes'] = 24.99
validate_prices['t-shirt'] = 9.99
validate_prices['blouse'] = 19.99

print(validate_prices['jacket'])
#! No Price Assigned

# Notice the following:
#
#   - We set the default value using a lambda expression.
#
#   - Any time we try to access a key that does not exist, it automatically
#     updates our defaultdict object by creating the new key-value pair
#     using the missing key and the default value.
#
# To read more about the defaultdict container, take a look at the
# Python Documentation: https://docs.python.org/3/library/collections.html#collections.defaultdics
#
# Now let's try using a defaultdict to validate new content on our clothing
# store website!


print('\nTasks\n--------')

# 1. We are updating an old version of our website to include new products that
#    we have for sale. We have a dictionary of all of the previous products
#    and locations on our site. The team has provided a list of all 
#    products our company sells including the new additions which are randomly
#    placed within the list. Use a defaultdict to validate which products are o
#    on the site and to automatically label those which are missing. For 
#    products which are missing, their values should default to 
#    'TODO: Add to website'.
#
#    For this first checkpoint, import the defaultdict from the collections
#    module and create a new variable called validated_locations. Use the
#    defaultdict constructor to create a new defaultdict object in 
#    validated_locations which defaults missing keys to have a value of
#    'TODO: Add to webiste'.
#
# 2. Not only can we create a defaultdict from scratch, but we can also create
#    one from an existing dictionary. To do this, we can use the .update()
#    method from the defaultdict class. This behaves the same way as the
#    .update() method from the dict class.
#
#    Take a look at the Python documentation for a refresher on the .update()
#    method. https://docs.python.org/3/library/stdtypes.html#dict.update
#
#    site_locations represents where each product exists on the clothing 
#    store webiste. 
#
#    Use the .update() method to move all of the site_location data into 
#    validated_locations.
#
# 3. We need to update the original dictionary with the new information.
#    Iterate through every item in the updated_products list and 
#    update the site_locations dictionary with the values from
#    validated_locations.
#
#    Print out site_locations to see the result!

# from collections import defaultdict

site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

validated_locations = defaultdict(lambda: "TODO: Add to website.")

validated_locations.update(site_locations)

for item in updated_products:
  site_locations[item] = validated_locations[item]

for key, value in sorted(site_locations.items()):
  print(f"{key} - {value}")

