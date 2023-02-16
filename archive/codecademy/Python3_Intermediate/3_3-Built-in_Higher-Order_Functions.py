# Learn Intermediate Python 3
# 3. Functions Deep Dive
# 3. Introduction to Higher-Order Functions
# Built-in Higher-Order Functions

print("\n --- What you'll be learning ---\n")
# ==============================================
#
# We've already learned about what defines higer-order functions, how to use
# them, and why they are useful. Now, we will get aquainted with Python's
# built-in high-order functions. We will take a look at three distinct 
# higher-order functions:
#
# 1. map()
# 2. filter()
# 3. reduce()
#
# Together, these three functions are some of the most used and powerful
# higher-order functions in Python and will help us elevate our Python
# programs!
#
print("\n --- Map --- \n")
# ===========================
# 
# The map() higher-order function has the following base structure:
#returned_map_object = map(function, iterable)
#
# When called, map() applies the passed function to each and every element
# in the iterable and returns a map object. The returned map object holds
# the result from applying the mapping function to each element in the 
# passed iterable. We will usually convert the map into a list to 
# enable viewing and further use. 
#
# map()
# map(function iterable)
# iterable = [1, 2, 3]
# returns object with the output of 
# function(1), function(2), function(3)
#
# Let's see what this looks like in practice if we wanted to double every value
# in a list of numbers
#
def double(x):
  return x * 2
int_list = [3, 6, 9]
doubled = map(double, int_list)
print(doubled)
# Output:
# <map at 0x7f1ca0f58090> - ok means i can iterate it at least
print(list(doubled))
#print(list(doubled)) - twice in a row, gone?
for i in doubled:
  if i > 0:
    print(i)
  else: 
    print("List is empty")
#
# Cool as heck! Own words :D 
# Hmmmm i take notice I can not print the variable twice. Is that normal? 
# Looks like it totally vanish after use. 
#
# In our example:
# 1. We defined a function called double() that takes in a value and returns
#    the value doubled. This function can be used anywhere in our program-
#    not only with map().
# 2. We also defined an iterable (int_list) that we wanted to apply the 
#    function to. 
# 3. We then passed the function reference double as the function argument
#    and int_list as the iterable to map()
# 4. The map() function proceeded to apply double() onto each element in
#    int_list
# 5. When we printed the result, we could see that the output of the map()
#    function was a specific type of object called map object. 
#
# If we want to see the actual results of mapping double() to the elements
# of int_list, we need to convert the map object to a list using built-in
# list() fucntion. 
#print(list(doubled))
# Oubput
# [6, 12, 18]
#
# Higher-order functions like map() work especially well with lambda functions.
# Because lambda functions are anonymous, we don't need to define a new named
# function for map() if that function won't be used again elsewhere. In this
# case, if we don't plan on reusing double() somewhere else in our program,
# we can rewrite double() function from the previous example with a 
# lambda function like so:
doubled2 = map(lambda input: input*2, int_list)
print(list(doubled2))
#
# Using a lambda function with map() produced the same output as when the
# custom double() function was passed to map(), but it only required one line
# of code instead of three.Now let's practice using map() to apply a lambda
# function to each element in a list. 
#
print("\n --- map() Code challenge ---\n")
# ===========================================
#
# Say we stored our course grades in a list, but some of the grades were on a
# four-point scale and others where on a 100-point scale. To get all the grades
# on the same scale, try using a lambda function with the map() function to 
# multiply just the grades on the four-point scale by 25 to get all of 
# the grades on the same 100-point scale. 
#
grade_list = [3.5, 3.7, 2.6, 95, 87]
fixed = map(lambda input: input*25 if isinstance(input, float) else input, grade_list)
print(list(fixed))
# Boom, correct first try. Also changed input<4 to isinstance(input, float)!
#
# 
print("\n\n --- filter() higher-order function ---\n")
# ====================================================
#
# Similar to map(), the filter() function takes a function and an iterable as
# arguments, Just as the name suggests, the goal of the filter() function is
# to "filter" values out of an iterable.
#
# The filter() function accomplishes this goal by applying a passed filtering
# function to each element in the passed iterable. The filtering function should
# be a function that returns a boolean value: True or False. The returned
# filter object will hold only those elements of the passed iterable for which
# the filtering function returned True.
#
# filter()
# filter(function, iterable)
# iterable = [3, 6, 9]
# function(3) returns True
# function(6) returns True
# function(9) returns False
# filter object then returns 3 and 6. 
#
# Let's see what this looks like in practice with a function that filters a 
# collection of names and returns only the names that start with the letter
# M or m:
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names)
print(list(M_names))
# Output
# ['margarita', 'Masako', 'Maki']
#
# In this example:
# 1. filter() takes two parameters: the lambda filtering function and the list,
#    names.
# 2. The filter() function then iterates through names and applies the lambda
#    function to each item in the list. 
# 3. For each item in the list, if the condition in the lambda function
#    evaluates to be True, the item is added to a filter object.
# 4. The filter object is returned and when converted to a list and printed,
#    we saw that it contained ['margarita', 'Masako', 'Maki'] - only M-names!
#
# Let's get some more practice using filter() with a lambda function.
#
#
#
print("\n --- filter() Code Challenge --- \n")
# ===============================================
#
# We were given a list of lists, where each sublist holds the title of a 
# famous book that has a year as its title and the last name of the author
# that wrote the book. Unfortunately, when this list was made, each of the books
# was accidentally entered twice-once with the title as a numeric value and 
# once with the title as a string. Use the filter() function to duplicate
# the list and keep only the sublists that have the book title stored 
# as a string:
books = [["Burgess", 1985], ["Orwell", "Nineteen Eighty-four"], ["Murakami", "1Q85"], ["Orwell", 1984], ["Burgess", "Nineteen Eight-five"], ["Murakami", 1985]]
fixx = filter(lambda name: type(name[1]) is str, books)
print(list(fixx))
#
# Boom! Got it, but through hint this time, as isinstance() did not do the trick. 
# Hint told me about type(), and that was a cleaner way to check anyways. 
#
#
#
print("\n\n --- reduce() Higher-Order Function \n")
# ===================================================
#
# Lastly, we have the reduce() function, which has two distinct differences
# from the built-in higher-order functions that we have learned so far.
#
# 1. In contrast to map() and filter() functions that are always available,
#    the reduce() function must be imported from the functools module to use
#    it. 
# 2. Rather than returning a reduce object as might be expected after learning
#    about and map() and filter(), reduce() returns a single value. To get to
#    this single value, reduce() cumulatively applies a passed function to
#    each sequential pair of elements in an iterable.
#
# reduce()
# reduce(function, iterable)
# function: returns x, returns y, returns z
# iterable = [3, 6, 9, 12]
# returns a single value of z
#
# Hmmmmm this is kinda clear as mud to me still.
#
# Let's see what this looks like in practice by using reduce() to multiply 
# together all the values in a list:
#
from functools import reduce
int_list = [3, 6, 9, 12]
reduce_int_list = reduce(lambda x,y: x*y, int_list)
print(reduce_int_list)
# Output:
# 1944 
# wtf ?!?!?!?!?!?!! 
#
# In this example:
# 1. The reduce() function takes two arguments: a lambda function and a list of
#    integers.
# 2. The lambda function takes 2 numbers, x and y and multiplies them together.
# 3. The reduce() function applies the lambda function to the first two
#    elements in the list, 3 and 6, to get a product of 18.
# 4. Next, 18 was multiplied by the following element in the list, 9, to get 162
# 5. Continuing on, 162 was multiplied by the next element, 12, to get 1944
# 6. The last, final value-1944-is what was returned by reduce()
#
# This process was essentially the same as multiplying 3*6*9*12
#
# Let's get some more practice using the reduce() function with a lambda function
# but with a list of strings this time.
#
# ! Ok this is really not clear to me. And get thrown into a challenge before 
# ! understanding wtf. lol.
#
print("\n --- reduce() Code Challnge --- \n") 
# ==============================================
#
# Given a list of letters, use the reduce() higher-order function with a lambda
# function to combine the letters into a single word:
# ! great, thats it lol. Thanks Codecademy.
#

letters = ['r', 'e', 'd', 'u', 'c', 'e']

fixxx = reduce(lambda x, y: x+y, letters)
print(fixxx)

# Ok seems like I overthink this one a bit? Looks like you just toss in
# two first items and it repeats that over the full list??
#
#
# Wrap up
# ===========

# Great Job! We learned all bout three really important built-in higher-order
# functions in Python! To summarize, we learned:
#
# 1. The map() function applies a passed function to each element in an
#    iterable and returns a map object
# 2. The filter() function applies a filtering function (a function that
#    returns a boolean) to each element in an iterable. filter() returns
#    filter object with only the elements for which the filtering function
#    returned True.
# 3. reduce() must be imported from the functools module. It reduces an
#    iterable to a single value by cumulatively applying a passed function
#    function to the first pair of elements in the iterable and then each
#    sequential element with the return value. 
# 4. These three functions streamline code on their own, but they are even
#    easier to read when they are used in conjunction with lambda functions.
#
# As we keep practicing and writing more code, these higher-order functions
# will make our code faster, more flexible, and easier to understand.

