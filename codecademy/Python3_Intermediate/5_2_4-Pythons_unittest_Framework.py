# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 4. Python's unittest Framework

print('''\n
Python's unittest Framework
----------------------------- ''')
# There are some problems with the approach to our previous unit tests that
# would make them difficult to maintain. First, we had to call each function
# specifically when a new test was created. We also didn't have any way of 
# grouping tests, which is necessary when the number of tests increases. 
# Perhaps most importantly, if one test failed, the AssertionError would
# prevent any remaining tests from running!
#
# Luckily, Python provides a framework that solves these problems and provides
# many other tools for writing unit tests. This framework lives in the 
# unittest module which is included in the standard library. It can
# be imported like so:

#! import unittest

# The unittest module provides us with a test runner. A test runner is a
# component that collects and executes tests and then provides results to 
# the user. The framework also provides many other tools for testing grouping,
# setup, teardown, dkipping and other features that we'll soon learn about.
#
# First, let's refactor our tests for the times_ten function to use the
# unittest framework. There are several things we need to do:
#
# First, we must create a class which inherits from unittest.TestCase, as
# follows:

#! import unittest
#!
#!class TestTimesTen(unittest.TestCase):
#!  pass

# This class will serve as the main storage of all our unit testing functions.
# Once we have the class, we need to change our test functions so that they are
# methods of the class. The unittest module requires that test functions begin
# with the word 'test', so our existing names work well:

#!import unittest
#!
#!class TestTimesTen(unittest.TestCase):
#!  def test_multiply_ten_by_zero(self):
#!    pass
#!
#!  def test_multiply_ten_by_one_million(self):
#!    pass
#!  
#!  def test_multiply_ten_by_negative_number(self):
#!    pass
  
# Lastly, we need to change our assert statements to use the assertEqual
# method of unittest.TestCase. The framework requires that we use special
# methods instead of standard assert statements. Don't worry we'll cover
# these methods in the remainder of this lesson, for now, simply get used to 
# the syntax. Here is what our class looks after the change

#!import unittest

#!def times_ten(number):
#!  return number * 10

#!class TestTimesTen(unittest.TestCase):
#!  def test_multiply_ten_by_zero(self):
#!    self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')
#!  
#!  def test_multiply_ten_by_one_million(self):
#!    self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')
#!  
#!  def test_multiply_ten_by_negative_number(self):
#!    self.assertEqual(times_ten(-10), -100, 'Expected times_ten(-10) to return -100')

# That's it! Now we can run our tests by calling unittest.main(). The unittest
# framework will work its magic to detect any tests in the existing module, run
# them, and provide us results. Our final code would look like this:

#!unittest.main()

#! Not gonna post the output. Too long!

# In the test output, we can see that two of the tests failed 
# (test_multiply_ten_by_one_million and test_multiply_ten_by_negative_number)
# 
# Let's get some practice with unittest by refactoring our previous test
# cases for Small World Air and then we will dive into learning all the useful
# testing methods we can work with!

print('''\n
Tasks
------------- ''')

# 1. First, let's import unittest at the top of the file.
#
# 2. Next, after the get_nearest_exit() function, create a class called
#    NearestExitTests. It should inherit from unittest.TestCase.
#
# 3. Refactor test_row_1(), test_row20(), and test_row_40() so that they
#    are methods of this class. Don't forget to add the self argument.
#
# 4. Change the assert statements in these function so that they instead
#    call the self.assertEqual() method with the correct arguments.
#
# 5. Remove the three function calls from the bottom of the file.
#    Replace them with a single call to unittest.main(). Observe
#    the output of our tests!
#
# 6. Looks like it's the same bug from before! Fix the error in the 
#    get_nearest_exit() function.
#    We should no longer get any failed tests when we run our script.

import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    location = 'back'
  return location

class NearestExitTests(unittest.TestCase):
  def test_row_1(self):
    self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is the front!')

  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')

  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')

unittest.main()

