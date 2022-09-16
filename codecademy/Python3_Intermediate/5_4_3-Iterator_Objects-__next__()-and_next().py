# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 3. Iterator Objects: __next__() and next()

print('''
Iterator Objects: __next__() and next()
------------------------------------------ ''')

# Now that we used an iterator's __iter__() method to create an iterator object,
# how does our for loop know which value to retrieve on each iteration?
#
# Well, the iterator object has a method called __next(), which retrieves the
# iterator's next value. Let's take a look using our SKU iterable for our
# shop:

sku_list = [7046538, 8289407, 9056375, 2308597]

sku_iterator = iter(sku_list)
next_sku = sku_iterator.__next__()
print(next_sku)
print(next_sku) # had to try lol, nope.

# Running this code would produce the following result for next_sku:

#! 7046538

# Similarly to __iter__() and iter(), there is a Python built-in function called
# next() that we can use in place of calling the __next__() method. Calling
# next() simply calls the iterator object's __next__() method. Here is the same
# script but using next:

sku_list = [7046538, 8289407, 9056375, 2308597]
sku_iterator = iter(sku_list)
next_sku = next(sku_iterator)
print(next_sku)

# Running this code is exactly the same as running the code above using the
# __next__() method and produces the same next_sku result:

#! 7046538

# But how does the iterator object know when to stop retrieving values? Does it
# keep calling __next__() forever? Well, luckily __next__() method will 
# raise an exception called StopIteration when all items have been iterated
# through.
#
# If we call __next__() a total of 5 times, one more than the total number of
# SKU's in our list, we will see the StopIteration exception raise on the
# last __next__() call:

#!print("\n")
#!sku_list = [7046538, 8289407, 9056375, 2308597]
#!sku_iterator = iter(sku_list)
#!for i in range(5):
#!  next_sku = sku_iterator.__next__()
#!  print(next_sku)

# Running this code will produce the following output:

#!7046538
#!8289407
#!9056375
#!2308597
#!Traceback (most recent call last):
#!  File "main.py", line 24, in <module>
#!    next_sku = sku_iterator.__next__()
#!StopIteration

# In summary, we can finally see why we needed to create the iterator object 
# in the previous exercise. Creating it, allows us to utilize next() or 
# __next__ to work with the stream of data one piece at the time.
#
# Now let's practice getting the hang of retrieving individual iterator 
# object values!

print('''\n 
Tasks
--------------- ''')
# 1. Using our dog food dictionary called dog_foods, create a variable called
#    dog_food_iterator that stores the value of calling iter() on our
#    iterable dog_foods.
#
# 2. Retrieve the first value of the dog_food_iterator using the built-in function
#    next() and set it to a variable called next_dog_food1
#
#    Print next_dog_food1 to see the result.
#
# 3. Retrieve the next two values of the dog_food_iterator using the __next__()
#    method and set them to the variables next_dog_food2 and next_dog_food3
#
#    Print both variables to see the results!
#
# 4. Uncomment the following line:
#    next(dog_food_iterator)
#
#    This will call next() on the dog_food_iterator object one more time.
#    What should we expect to see in the output? Run the code to find out!

# --------------------

dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pup Foods": 8
}

dog_food_iterator = iter(dog_foods)
next_dog_food1 = next(dog_food_iterator)
next_dog_food2 = next(dog_food_iterator)
next_dog_food3 = dog_food_iterator.__next__()

print(next_dog_food3)
print(next_dog_food2)
print(next_dog_food1)

# next(dog_food_iterator)

# Hmm is this a better way to refrence specific items in a list etc? 
