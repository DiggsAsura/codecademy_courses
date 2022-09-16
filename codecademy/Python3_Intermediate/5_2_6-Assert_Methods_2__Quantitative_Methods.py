# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 6. Assert Methods II: Quantitative Methods

print('''\n
Assert Methods II: Quantitative Methods
------------------------------------------ ''')

# Often we need to test conditions related to numbers. The unittest module 
# provides a handful of assert methods to achieve this. Let's take a look at two
# common assert methods related to quantitative comparisons, their general
# syntax, as well as their assert statement equivalents.
#
# - assertLess: The assertLess() method takes two arguments and checks that
#   the first argument is less than the second one. If it is not, the test
#   will fail.
#
#!  self.assertLess(value1, value2)
#
# - assertAlmostEqual: The assertAlmostEqual() method takes two arguments and
#   checks that their difference, when rounded to 7 decimal places, is 0. In
#   other words, if they are almost equal. If the values are not close enough 
#   to equality, the test will fail.
#
#! self.assertAlmostEqual(value1, value2)
#
# The equivalent assert statements would be the following

#    Method                               Equivalent
#    self.assertLess(2, 5)                assert 2 < 5
#    self.assertAlmostEqual(.22, .225)    assert round(.22 - .225, 7) == 0

# The full list of quantitative methods can be seen in the Python documentation
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.output
# Let's put these methods into practice!


print('''\n
Tasks
-------------- ''')

# 1. Our entertainment.py file has a function called get_maximum_display_brightness()
#    that returns the max screen brightness value.
#
#    Create a test method called test_maximum_display_brightness(). Inside the
#    method, do the following:
#
#     1. Call entertainment.get_maximum_display_brightness() and store the
#        return value in a variable called brightness
#
#     2. Next, call self.assertAlmostEqual() to make sure that brightness
#        is almost equal to 400
#
# 2. Our entertainment2.py file has a method called 
#    entertainment.get_device_temp() that returns the current 
#    temperature. 
#
#    Create a test method called test_device_temperature(). Inside the method
#    do the following:
#
#     1. Call entertainment2.get_device_temp() and store the return value
#        in a variable called device_temp
#
#     2. Then call self.assertLess() to make sure that device_temp is 
#        less than 35

import unittest
import entertainment2

class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = entertainment2.get_daily_movie()
    licensed_movies = entertainment2.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = entertainment2.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Write your code below:
  def test_maximum_display_brightness(self):
    brightness = entertainment2.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)
  
  def test_device_temperature(self):
    device_temp = entertainment2.get_device_temp()
    self.assertLess(device_temp, 35)
    

unittest.main()



