# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Function Arguments
# 7. Function Call Unpacking & Beyond

# Hopefully, by now, we have started to see the power of using the * and ** operators in our
# function definitions. However, Python doesn't stop there! Not only can we use the operators
# when defining parameters, but we can also use them in function calls.
#
# Let's imagine we want to sum a few numbers together:
#def sum(num1, num2, num3):
#  print(num1 + num2 + num3)
#
# Right now, our function forces us to pass in an individual argument for num1, num2 and num3. This
# isn't a big issue if we have separate variables or know our numbers in advnace. However,
# what if we wanted to use a list like [3, 6, 9] instead? Well, that is where the unpacking
# operators comes to the rescue.
#
# Let's observe:
my_num_list = [3, 6, 9]

def sum(num1, num2, num3):
  print(num1 + num2 + num3)

sum(*my_num_list)
# 
# Would output
# 18
#
# We can even use the operators inside of built-in functions. For example, instead of manually 
# providing the range() built-in function with a start and stop value, we can unpack a list 
# directly into it. Let's take a look:
start_and_stop = [3, 6]
range_values = range(*start_and_stop)
print(list(range_values))
#
# Would output:
# [3, 4, 5]
#
# The possibilities of using the * and ** operators are endless. Observe some more clever use
# cases: 
# 
#   - Unpacking parts of an iterable
a, *b, c = [3, 6, 9, 12, 15]
print(b)
# 
# Would output: 
# [6, 9, 12]
#
#   - Merging iterables
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)
#
# Would output
# (0, 3, 6, 9, 12)
#
# Combining unpacking and packing
num_collection = [3, 6, 9]

def power_two(*nums):
  for num in nums:
    print(num**2)
power_two(*num_collection)
# 
# Would output
# 9
# 36
# 81
#
# Let's see how we can apply some of these use cases to make Jiho's resturant application better!
#

# Tasks 
# 1. Jiho thinks our resturant application is missing one really important feature. Jiho would
#    like for the application to be able to calculate the total bill of a table (including tip)
#    and split it based on the number of people at the table. 
# 
#    Thankfully, we had an existing function called calculate_price_per_person() from our last
#    resturant project that we can reuse. Take some time to examine the function and its 
#    inner workings. 
# 
#    Run the code to move onto the next checkpoint. Don't worry we shouldn't see any output
#    just yet. 
#
# 2. Looks like we are ready to give our function a test run! Luckily, table seven at Jiho's 
#    resturant is ready to pay. 
#
#    Define a list called table_7_total that has the following values in order:
#     - 534.50 (Representing the total bill cost)
#     - 20.0 (Representing the tip percentage)
#     - 5 (Representing the number of people to split the bill for)
#
# 3. Using the unpacking operator, call calculate_price_per_person() with the list table_7_total

def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

table_7_total = [534.50, 20.0, 5]

calculate_price_per_person(*table_7_total)

# Ok! Easy lesson, but it really starts to unfold the power of * and ** :D