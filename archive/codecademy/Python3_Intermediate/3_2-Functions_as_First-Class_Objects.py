# Learn Intermediate Python 3
# 3. Functions Deep Dive
# 2. Introduction to Higher-Order Functions
# Functions as First-Class Objects

# So far, we have explored the core benefits of using functions in our 
# programs. We have seen firsthand how using functions allows for better code
# modularity, readability, and extensibility. Many of these benefits stem
# from the ability of functions to be extremely flexible. In Python, functions
# are treated just like any other object, which in turn gives them the power
# to be used in a variety of ways. In order to truly understand the power of
# functions, let's explore what it means for functions to be objects!
#
# In Python, all functions, including the ones we're written, are classified
# as first-class objects (sometimes also called first-class citizens or
# first-class functions).
# This means they have four important characteristics:
#
# 1. First-class objects can be stored as variables
# 2. First-class objects can be passed as arguments to a function
# 3. First-class objects can be returned by a function
# 4. First-class objects can be stored in data structures (e.g., lists, dictionaries, etc)
#
# We may have taken this functionality for granted before if we ever assigned
# a function to a variable or stored a function in a list, like these examples:
#
# Here, we assign a function to a variable
#uppercase = str.upper
# And then call it
#big_pie = uppercase("pumpkinpie")
#print(big_pie)
#
# Here we store two functions in a list
#string_manipulation_functions = [str.upper, str.lower]
#
# But the fact that functions are first-class objects in Python, and therfore 
# have all the flexibility of objects, enables us to write even more powerful 
# types of functions called higher-order functions.
#
# Higher-order functions operate on other functions via arguments or via
# return values. This means higher-order functions can do one or both of
# the following:
# 
# - Accept a function as an argument
# - Have a return value that is a function
#
# Let's dive into each of these properties to see this special type of function
# in action!
#
#
# Functions as Arguments
# =========================
#
# Let's start with higher-order functions that take another function as an 
# argument. We'll go through a series of examples using a higher-order function,
# total_bill(), that takes another function as one of its arguments. This
# function aims to use other functions (taken in as arguments) to calculate the
# total bill at say a returant or cafe. By examining each example in turn, we
# will learn how to use higher-order functions and why exactly they are so
# powerful. Later on, we will come back to higher-order functions that have
# a function as a return value. 
# Here we go!
#
# Take a look at the example higher-order function called total_bill():
def total_bill(func, value):
  total = func(value)
  return total

# The total_bill() function takes two arguments: func and value. When called,
# total_bill() applies func() to value and returns the result. In order to see
# it in action, let's define a function called add_tax(), and then pass it
# to our higher-order total_bill() function along with a numeric value:
print("\n --------------- \n")
def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return new_total

print(total_bill(add_tax, 100))
# Output:
# 106.0
#
# Here, total_bill() is classified as a higher-order function because it takes
# in an argument that is a function (add_tax() in the above example). Right off
# the bat, this setup may not be very useful compared to simply calling 
# add_tax(100) directly, but what if we wanted to add a tip instead of tax?
# Let's see how we can reuse our higher-order function to add a 20% gratuity
# instead of 6% sales tax:
#
print("\n --------------- \n")
def add_tip(total):
  tip = total * .2
  new_total = total + tip
  return new_total

print(total_bill(add_tip, 100))
# Output
# 120.0
#
# We can see that we can reuse total_bill() for both of these functions! But
# this still isn't any more useful than calling the function add_tax() or
# add_tip() directly on a value. The true power comes when we want to keep a 
# consistent manipulation no matter what function is passed in. We can see this
# if we modify our total_bill() function so it adds a formatting to our the
# total amount wed in a consistent and friendly way, regardless of which 
# function is passed in:
#
print("\n --------------- \n")
def total_bill2(func, value):
  total = func(value)
  return ("The total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

print(total_bill2(add_tax, 100))
print(total_bill2(add_tip, 100))
#
# Output:
# The total amount owed is $106.00. Thank you! :)
# The total amount owed is $120.00. Thank you! :)
#
# Now, no matter the function we pass as the argument and the behaviour we 
# want the function to accomplish, we can always consistently format the 
# total and add a friendly message to the returned result. While we are
# only adding on a small manipulation at this point, we can really do consistent
# manipulation that increases our code reuse and makes our programs more 
# modular. This isn't the only situation where higher-order functions shine,
# they are also fantastic for situations involving iteration!
#
#
#
# Functions as Arguments - Iteration
# =====================================
#
# Let's return to our total_bill() example. Now say we have a list of bills
# instead of just one, and we want to add tax or tip to each bill, depending 
# on the type of sale it is. 
# 
# One way to accomplish this could be to write out separate loops: one for
# sales that need to have tax added and one for sales that should have
# a tip added. To get a sense of what this would look like, let's write out the
# loop for adding tax first:
#
print("\n --------------- \n")
bills = [115, 120, 42]
new_bills = []

for i in range(len(bills)):
  total = add_tax(bills[i])
  new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

print(new_bills)
#
# Output:
# ['The total amount owed is $106.00. Thank you! :-)', 'The total....., 'The total.....']
#
# Now, we could write out another loop for when we need to add a tip instead of
# tax, but we can probably guess how many repititions would be involved. A
# much more powerful solution would be to use a higher-order function to apply
# add_tax() or add_tip() to each balance in our list. Let's first define
# a higher-order function, total_bills(), that takes a function and a list as
# arguments, applies the function to each element in the list, standardizes the
# format of the result and adds a friendly message, appends the output to a new
# list, and finally returns the updated new list:
#
print("\n --------------- \n")
def total_bills(func, list):
  new_bills = []
  for i in range(len(list)):
    # Here we apply the function to each element of the list!
    total = func(list[i])
    new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you :)")
  return new_bills

# Next, let's use the add_tax() function that we wrote before with our new
# total_bills() higher-order function:
bills2 = [115, 120, 42]
bills_w_tax = total_bills(add_tax, bills2)
print(bills_w_tax)

# Output:
# ['Total amount owed is $121.90. Thank you! :)',
# 'Total amount owed is $127.20. Thank you! :)',
# 'Total amount owed is $44.52. Thank you! :)']
#
# And if we needed to add a tip instead of tax, we could simply swap out the
# function argument
#

bills_w_tip = total_bills(add_tip, bills2)
print(bills_w_tip)
#
# As these examples show, being able to pass functions in as arguments can be
# pretty handy, especially when we want to apply a function multiple times. 
# In fact, it's so handy that there's a built-in higher-order function in
# Python that does just that-the map() function. We will learn more about
# the map() function in upcoming articles. Now that we have explored functions
# as arguments, let's turn towards higher-order functions that have functions
# as return values. 
#
# 
print("\n --------------- \n")
# Functions as Return Values
# =============================
#
# So far, we have focused on higher-order functions that take another function
# as an argument. Remember, though, that a function that returns another 
# function is also a higher-order function. Let's see what this looks like
# in practice by considering a higher-order function, make_box_volume_function(),
# that will help us calculate the volums of boxes when they have the same
# height:
def make_box_volume_function(height):
  # defines and returns a function that makes two numeric arguments,
  # length & width, and returns the volume given the input height
  def volume(length, width):
    return length*width*height
  return volume

box_volume_height15 = make_box_volume_function(15)
print(box_volume_height15(3,2))
# 
# Output: 
# 90
#
# And if we had slightly shorter boxes:
box_volume_height10 = make_box_volume_function(10)
print(box_volume_height10(3,2))
#
# Output:
# 60
#
# In the example, we wrote a higher-order function, make_box_volume_function()
# that takes a height as an argument and returns a new function that calculates
# the volume of any box with that height when it is passed the length and width
# of the box. As we can see, higher-order functions with functions as
# return values are just as reusable as higher-order functions with functions as
# arguments and, therfor, also reduce repetition and the chances for 
# mistakes to creep into code. Our appreciation for this will grow as we 
# keep writing more code and our code becomes increasingly complex!
#
#
# =====
# Wrap Up 
# ==========
#
# Great Job! We have explored many new concepts surrounding higher-order 
# functions! To summarize, we learned:
# 
# 1. Higher-order functions are possible because functions are first-class 
#    objects in Python, meaning that a function can be stored as a variable, 
#    passed as an argument to a function, returned by a function, and 
#    stored in data structures (lists, dictionaries, etc)
#
# 2. Higher-order functions are functions that operate on other functions
#    by taking another function as an argument, returning another function, or both
#
# 3. Higher-order functions can reduce repetition in code, making code easier
#    to read and less prone to mistakes. 
#
# As you keep practicing and writing more code, higher-order functions will
# make your code faster, more elegant, and easier for collaborators to 
# understand and reuse. Next up, we'll learn about several built-in
# higher-order functions in Python!