# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 3. Unit Testing

print('''\n
Unit Testing
-------------- ''')
# Assertion statements are a good start to ensuring our programs are being
# tested, but they don't necessarily tell us what we should test. Generally,
# we can start by testing the smallest unit of a program.
#
# For example, in the real world, if we were testing the functionality of a door,
# we could test a multituede of units. The handle could be an example of a single
# unit that we must check to make sure a door functions, followed by the hinges
# and maybe even the lock.
#
# In programming, these types of individual tests are called unit tests. Like
# our door handle, we can test a single unit of a program, such as a function,
# loop, or variable. A unit test validates a single behavior and will make sure
# all of the units of a program are functioning properly.
#
# Let's say we wanted to test a single function (a single unit). To test a single
# function, we might create several test cases. A test case validates that a
# specific set of inputs produces an expected output for the unit we are trying
# to test. Let's examine a test case for our times_ten() function from the
# previous excercise:

# The unit we want to test
def times_ten(number):
  return number * 100

# A unit test function with a single test case
def test_multiply_ten_by_zero():
  assert times_ten(0) == 0, 'Expected times_ten(0) to return 0'

# Great, now we have a simple test case that validates that times_ten() is
# behaving as expected for a valid input of 0! We can improve our testing
# coverage of this function by adding some more test cases with different inputs.
# A common approach is to create test cases for specific edge case inputs as 
# well as reasonable ones. Here is an example of testing two extreme inputs:

def test_multiply_ten_by_one_million():
  assert times_ten(1000000) == 10000000, 'Expected times_ten(1000000) to return 10000000'

def test_multiply_ten_by_negative_number():
  assert times_ten(-10) == -100, 'Expected times_ten(-10) to return -100'

# Now we have several test cases for a wide variety of inputs: a large
# number, a negative number, and zero. We can create as many test cases
# as we see fit for a single unit, and we should try to test all the unique
# types of inputs our unit will work with.
#
# Now, let's create a variety of unit tests for another feature of 
# Small World Air. 

print('''\n
Tasks
-------- ''')
# 1. At Small Air World, every plane seat has a monitor which displays
#    nearest emergency exit. 
#
#    This monitor relies on a function called get_nearest_exit(),
#    which takes a row number and then returns an exit location depending
#    on where the row is. Let's make sure our function is working properly
#    by creating a unit test.
#
#    Create a function called test_row_1() that will host a test case.
#    Inside the function, assert that a call of get_nearest_exit(1) should
#    equal to 'front', along with a message, 'The nearest exit to row 1
#    is in the front!'.
#
# 2. Create another test case function called test_row_20().
#
#    Inside the function, call get_nearest_exit(20) and assert that the return
#    value is equal to middle, along with the message, 'The nearest exit to row
#    20 is in the middle!'
#
# 3. Finally, create another test case function called test_row_40()
#
#    Inside the function, call get_nearest_exit(40) and assert that the return
#    value is equal to 'back', along with the message, 'The nearest exit to row
#    40 is in the back!'
#
# 4. At the bottom of the file, call each of the three test functions we 
#    created. What would be the expected output?
#
# 5. Looks like our tests caught a logic error in our function get_nearest_exit()!
#    If the row nuber is larger than 30, we actually want to return 'back'.
#
#    Adjust the function and fix the error so all of our tests pass (we should
#    see no output)

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

def test_row_1():
  assert get_nearest_exit(1) == 'front', 'The nearest exit to row 1 is in the front!'

def test_row_20():
  assert get_nearest_exit(20) == 'middle', 'The nearest exit to row 20 is in the middle!'

def test_row_40():
  assert get_nearest_exit(40) == 'back', 'The nearest exit to row 40 is in the back!'
  
test_row_1()
test_row_20()
test_row_40()
