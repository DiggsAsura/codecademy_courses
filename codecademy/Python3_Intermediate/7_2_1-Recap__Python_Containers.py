# 7. Specialized Collections
# 2. Collections
# 1. Recap: Python Containers

from copyreg import remove_extension


print('\nRecap: Python Containers\n----------------------------')

# In Python, there are many ways to store and organize data. So far, we have
# experienced adding elements to a list, writing key-value pairs to a dictionary,
# or even accessing data with tuples.
#
# Any object which stores data is called a container. If you have writting code
# in Python, you have likely been using containers this whole time!
#
# We are familiar with Python's built-in containers (such as lists or dictionaries),
# but there are many other containers that exist in Python. These containers each
# specialize in a specific job and can be imported into your code from other 
# modules or even be custom-made! In this lesson we will be looking at these
# specialized containers from the Python collections module.
#
# We will start to dive deeper in the next exercises, but for now, let's take 
# some time to review some of the common built-in containers we are most
# familiar with:
#
#* Lists
#
# Lists are an ordered group of elements. Elements can be added, removed, 
# accessed and modified.

products = ['t-shirt', 'pants', 'shoes', 'dress', 'blouse']

products.append(('jacket'))
products.sort()
products.remove('shoes')
print(products)


#* Tuples
#
# Tuples are immutable objects which group multiple elements together. They
# are similar to lists, except that they cannot be modified once created.

searched_terms = ('clotes', 'phone', 'app', 'purchsae', 'clothes', 'store', 'app', 'clothes')

term = searched_terms[2]
num_of_occurrences = searched_terms.count('clothes')

print(searched_terms)
print(term)
print(num_of_occurrences)


#* Dictionaries
#
# Dictionaries are unordered groups of key-value pairs:

orders = {
  'order_4829': {
    'type': 't-shirt',
    'size': 'large',
    'price': 9.99,
  },
  'order_6184': {
    'type': 'pants',
    'size': 'medium',
    'price': 14.99,
  }
}

order_4829_price = orders['order_4829']['price']
order_6184_size = orders['order_6184']['size']
orders['order_4829']['size'] = 'x-large'
num_or_orders = len(orders)

print(order_4829_price)
print(order_6184_size)
print(orders)
print(num_or_orders)


#* Sets
#
# Sets are unordered groups of elements that cannot contain duplicates, elements
# cannot be modified.

old_products_set = {'t-shirt', 'pants', 'shoes'}
new_products_set = {'t-shirt', 'pants', 'blouse', 'dress'}
updated_products = new_products_set | old_products_set
removed_products_set = old_products_set - new_products_set

print(old_products_set)
print(new_products_set)
print(updated_products)
print(removed_products_set)


# You can learn more about these built-in containers in earlier lessons or in 
# the Python Documentation https://docs.python.org/3/tutorial/datastructures.html
#
# Now that we have reviewed the most common containers in Python, let's practice
# using them, and then move on to exploring the specialized containers we 
# mentioned earlier!



print('\nTasks\n------------')

# 1. We've decided to make an application in Python to help our friend's clothing
#    company. To begin, let's use some of Python's built-in containers to set
#    up our company info!
#
#    First, create a variable called company_name which contains a string
#    representing our clothing company's name. Come up with something creative!
#
# 2. Next, create a tuple called company_location which contains two decimal
#    values for latitude and longitutde. Feel free to use any coordinates.
#
# 3. Create a list of strings called company_products representing which products
#    we will be selling in our store. Make sure there are at least 5 products.
#
# 4. Finally, create a dictionary that will store all of the previous valules
#    we created into a variable called company_data.
#
#    Use the keys name, location, and products with the values being respective
#    variables we created in the last steps. 

company_name = "Kenny's Clothing"
company_location = (12345, 56789)
company_products = ['sneakers', 't-shirts', 'hoddies', 'pants', 'socks']

company_data = {
  'name': company_name,
  'location': company_location,
  'products': company_products
}

print(company_data)