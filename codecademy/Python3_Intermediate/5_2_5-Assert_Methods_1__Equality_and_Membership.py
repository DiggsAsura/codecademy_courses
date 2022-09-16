# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 5. Assert Methods I: Equality and Membership


print('''\n
Assert Methods I: Equality and Membership
------------------------------------------- ''')
# In the last exercise, we saw how to check for equality between two values in
# the unittest framework using the .assertEqual method of the TestCase class.
# The framework relies on built-in assert methods instead of assert statements
# to track results without actually raising any exceptions. Specific assert
# methods take arguments instead of a condition, and like assert statements,
# they can take an optional message argument.
#
# Let's go over three commonly used assert methods for testing equality and
# membership, their general syntax, and their assert statement equivalents.
#
# - assertEqual: The assertEqual8) method takes two values as arguments and
#   checks that they are equal. If they are not, the test fails.
#
#!  self.assertEqual(value1, value2)
#
# - assertIn: The assertIn() method takes two arguments. It checks that the first
#   argument is found in the second argument, which should be a container.
#   If it is not found in the container, the test fails.
#
#!  self.assertIn(value, container)
#
# - assertTrue: the assertTrue() method takes a single argument and checks that
#   the argument evaluates to True. If it does not evaluate to True, the test 
#   fails.
#
#! self.assertTrue(value)
#
# The equivalent assert statements would be the following:

# Method                           Equivalent
# self.assertEqual(2, 5)           assert 2 == 5
# self.assertIn(5, [1, 2, 3])      assert 5 in [1, 2, 3]
# self.assertTrue(0)               assert bool(0) is True

# The full list for equality and membership can be seen in the Python
# documentation. Let's put these methods into practice!

print('''\n
Tasks 
-------------- ''')

# 1. Small World Air planes are equipped with an on-board entertainment system
#    which we need to create some tests for. Take some time to review
#    entertainment.py and tests.py
#
#    Note the three functions in entertainment.py:
#
#     1. get_daily_movie():
#        returns the movie of the day.
#
#     2. get_licensed_movies():
#        returns a list of licensed movies the plane can play.
#
#     3. get_wifi_status():
#        returns the current wifi status on the plane.
#
#    Note the two test cases in tests.py
#
#     1. test_movie_license(): 
#        is intended to test if a daily movie is licensed
#
#     2. test_wifi_status():
#        is intended to test if the wifi is currently active
#
#    Run the code to proceed.
#
# 2. Every flight has a free movie. We want to create a test that checks
#    our database to make sure that the uploaded movie has a valid license,
#    or else we could pay some hefty fines.
#
#    Inside of our test_movie_license() test method, we have two variables 
#    defined:
#
#     - daily_movie: which stores the value of the current free daily movie
#
#     - licensed_movies: which stores the value of all the current licensed
#       movies.
#
#    To test if we have a license for the current daily movie, we need to 
#    compare if daily_movie exists inside of licensed_movies.
#
#    Use the self.assertIn() assert method inside of test_movie_license() to 
#    check if the daily_movie is licensed.
#
# 3. Our entertainment system also provides WiFi as a purchase option for 
#    passengers. We want to make a test that ensures the WiFi is enabled.
#
#    Inside the test method called test_wifi_status() we have a variable 
#    called wifi_enabled which stores the boolean value of wheter the wifi is
#    turned on or not. 
#
#    Use the self.assertTrue() assert method inside of test_wifi_status() to
#    test that wifi_enabled is True. The test should fail because currently 
#    wifi is diabled.

import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)
  
  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

unittest.main()

# Boom, got this!