# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 10. Skipping tests

print('''\n
Skipping tests
------------------ ''')

# Sometimes we have tests that should only run in a particular context. For 
# example, we might have a group of tests that only runs on the Windows operatin
# system but no Linux or macOS. For these situations, it's helpful to be able to 
# skip tests. 
#
# The unittest farmework provides two different ways to skip tests:
#
#   1. The @unittest skip decorator
#
#   2. The skipTest() method
#
# First, let's examine the skip decorator option. There are two decorator options
# to accomplish the goal of skipping a test. Let's observe both of them in the
# example below:

#!import sys
#!import unittest
#! 
#!class LinuxTests(unittest.TestCase):
#! 
#!    @unittest.skipUnless(sys.platform.startswith("linux"), "This test only runs on Linux")
#!    def test_linux_feature(self):
#!        print("This test should only run on Linux")
#! 
#!    @unittest.skipIf(not sys.platform.startswith("linux"), "This test only runs on Linux")
#!    def test_other_linux_feature(self):
#!        print("This test should only run on Linux")

# Let's break down both skip decorator options:
#
#   - The skipUnless option skips the test if the condition evaluates to False.
#
#   - The skipIf option skips the test if the condition evaluates to True.
#
# Both share common requirements. Firstly, both of these skip decorators are
# prefaced with @unittest to denote the decorator pattern. They both take a
# condition as the first argument, followed by a string message as the second.
# In this example, both decorators achieve the same goal: skipping the test if
# the operating system is not Linux. 
#
# If we ran the tests on a macOS system, we would get the following output:

#!ss
#!----------------------------------------------------------------------
#!Ran 2 tests in 0.000s
#! 
#!OK (skipped=2)

# The second way to skip tests is to call the skipTest method of the TestCase
# class, as in this example:

#!class linuxTests(unittest.TestCase):
#!  
#!  def test_linux_feature(self):
#!    if not sys.platform.startswith("linux"):
#!      self.skipTest("Test only runs onLinux")

# Here we call self.skipTest() from within the test function itself. It takes
# a single string message as its argument and always causes the test to be skipped
# when called. When run on macOS we get the following output:

#!s
#!----------------------------------------------------------------------
#!Ran 1 test in 0.000s
#! 
#!OK (skipped=1)

# Skip decorators are slightly more convenient and make it easy to see under
# what condidtions the test is skipped. When the conditions for skipping a test
# are too complicated to pass into a skip decorator, the skipTes method is
# the recommended alternative.
#
# Let's practice skipping tests in our Small World Air application!

print('''\n
Tasks 
-------------- ''')

# 1. Small World Air continues to grow! They recently added some regional jets
#    for shorter flights. Unfortunately, these planes don't have an onboard
#    entertainment system.
#
#    Let's modify our EntertainmentSystemTests to make sure these tests get
#    skipped on regional jets. Use the @unittest.skipIf() decorator to 
#    test_movie_liscense()
#
#    It should skip the test if entertainment.regional_jet() returns True. The
#    message should output 'Not available on regional jets'.
#
# 2. Add the @unittest.skipUnless decorator to test_wifi_status().
#
#    It should skip the test unless entertainment.regional_jet()
#    returns False. The message should be 'Not available on regional jets'.
#
# 3. Inside of test_device_temperature(), add an if statement which calls
#    entertainment.regional_jet(). If the return value is True,
#    then call self.skipTest() with an argument of 'Not available on 
#    regional jets'.
#
#    Add the same if block to test_maximum_display_brightness()

import unittest
import entertainment4

class EntertainmentSystemTests(unittest.TestCase):

  @unittest.skipIf(entertainment4.regional_jet(), 'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment4.get_daily_movie()
    licensed_movies = entertainment4.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  @unittest.skipUnless(entertainment4.regional_jet() is False, 'Not available on regional jets')
  def test_wifi_status(self):
    wifi_enabled = entertainment4.get_wifi_status()
    self.assertTrue(wifi_enabled)

  def test_device_temperature(self):
    if entertainment4.regional_jet() is True:
      self.skipTest('Not available on regional jets')
    device_temp = entertainment4.get_device_temp()
    self.assertLess(device_temp, 35)

  def test_maximum_display_brightness(self):
    if entertainment4.regional_jet() is True:
      self.skipTest('Not available on regional jets')
    brightness = entertainment4.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)


unittest.main()