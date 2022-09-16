# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 2. Iterator Objects: __iter__() and iter()

print('''\n
Iterator Objects: __iter__() and iter()
---------------------------------------- ''')

# Let's return to our for loop from before:

dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Foods": 8
}

for food_brand in dog_foods:
  print(f'{food_brand} has {dog_foods[food_brand]} bags')

# Under the hood, the first step that the for loop has to do is to convert our
# dictionary (the iterable) of dog_foods to an iterator object. An iterator
# object is a special object that represents a stream of data that we can 
# operate on. To accomplish this, it uses a built-in function called
# iter():

dog_food_iterator = iter(dog_foods)

# We can see the new object by printing it:

#!print(dog_food_iterator)

# Output
# <dict_keyiterator object at 0x....> 
# 
# Note: The memory address is omitted since it varies on the system you run the script on. 

# Here is a visual representation, using the graphic we saw earlier


#  - iter()
# |  next()
# |  StopIteration
# |
# |
# |
# |                  Iterator object:
#  ----------------> iter(dog_food)    The for loop uses the iter() function
#                                      to convrt dog_food into an iterator object


# To go behind the scenes even further, iter(dog_foods) is actually calling a 
# method defined within the iterable called __iter__(). All iterables have this
# __iter__() method defined. We can even use the Python built-in function dir()
# to show that our dog_foods dictionary (iterable) has a defined method
# called __iter__()

#!print(dir(dog_foods))

# If we examined the output (shortened for brevity), we can spot the __iter__
# property
#
# In summary, the __iter__() method simply returns the iterator object that allows
# us to iterate over the iterable.Calling dog_foods.__iter__() will retreive
# the same iterator object as calling iter(dog_foods). This means that the
# built-in function iter() and the iterable's method __iter__() can be used
# interchangeably. While the object itself might not seem super useful just yet,
# we'll see how to manipulate the stream of data inside of it in the next
# exercieses.
#
# Now that we have taken a peek under the hood, let's practice creating our own
# iterator objects from iterables using iter() and __iter__()

print('''
Tasks 
---------- ''')

# 1. Suppose we have a list of SKUs (stock-keeping units) for products in our
#    pet shop. Let's examine the internal methods of the iterable sku_list.
#
#    Use dir() on sku_list and print out the result. Can you spot the 
#    __iter__ in the list of methods that are printed?
#
# 2. Let's access the internal __iter__() method from sku_list to create
#    our iterator object.
#
#    Create a variable called sku_iterator_object_one that is equal to calling
#    .__iter__() on sku_list.
#
#    Lastly, print sku_iterator_object_one
#
# 3. Finally, let's use the alternative iter() function to create an iterator
#    object from sku_list
#
#    Create a variable called sku_iterator_object_two that is equal to 
#    calling iter() on sku_list.
#
#    Lastly, print sku_iterator_object_two!
#
#    Observe that both methods will be able to retrieve an iterator object but
#    it's always helpful to know that iter() uses __iter__ under the hood.

sku_list = [7046538, 8289407, 9056375, 2308597]

#print(dir(sku_list))

sku_iterator_object_one = sku_list.__iter__()
print(sku_iterator_object_one)

sku_iterator_object_two = iter(sku_list)
print(sku_iterator_object_two)

