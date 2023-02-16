# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 7. Assert Methods III: Exception and Warning Methods

print('''\n
Assert Methods III: Exception and Warning Methods
--------------------------------------------------- ''')

# There is another group of assert methods related to exceptions and warnings.
# Note that while we haven't covered warnings in detail yet, they are a type
# of exception. Let's go over two of these methods and their general syntax.

#   - assertRaises: The assertRaises() method takes an exception type as its
#     first argument, a function reference as its second, and an arbitrary
#     number of arguments as the rest.
#
#     It calls the function and checks if an exception is raised as result. The
#     test passes if an exception is raised, is an error if another exception is 
#     raised, or fails if no exception is raised. This method can be used
#     with custom exceptions as well!
#
#!    self.assertRaises(specificException, function, functionArguments...)
#
#   - assertWarns: The assertWarns() method takes a warning type of its first
#     argument, a function reference as its second, and an arbitrary number
#     of arguments for the rest.
#
#     It calls the function and checks that the warning occurs. The test passes
#     if a warning is triggered and fails if it isn't.
#
#!    self.assertWarns(specificWarningException, function, functionArguments...)
#
# There are no particular concise ways to replicate these tests using the assert
# keyword so it is recommended to use these methods instead when possible!
#
# The ful llist of exception and warning methods can be seen in the Python
# documentation: https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance
# Let's put these methods into practice!


print('''\n
Tasks
------------ ''')

# 1. We need to create some tests for the airplane alert system so that the flight
#    crew is properly notified of critical events.
#
#    Let's start by creating a class called SystemAlertTests which inherit
#    from unittest.TestCase
#
# 2. We are going to create a test for any power outages that might occur on
#    the airplane. Check out the custom exception PowerError and our function
#    that raises the error power_outage_detected() in the alerts.py for us
#
#    In our SystemAlertTests class, create a test method called test_power_outage_alert()
#
#    Inside the new method, use self.assertRaises() to check that an
#    alerts.PowerError is raised whenever alerts.power_outage_detected is called 
#    with an argument of True
#
#    This test should pass since we are passing a value of True and the exception
#    is raised.
#
# 3. We are going to create a test for any water level warnings that occur on
#    the airplane. Check out the custom exception WaterLevelWarning and our
#    function that raises the warning water_levels_check() in the
#    alerts.py file. The file is already imported into tests.py for us.
#
#    In our SystemAlertTests class, create a test method called
#    test_water_levels_warning().
#
#    Inside the new method, use self.assertWarns() to check that an 
#    alerts.WaterLevelWarning is raised whenever alerts.water_levels_check is
#    called with an argument of 150 liters.
#
#    This test should pass since we are passing a value less than 200 and
#    warning occus.

import unittest
import alerts

class SystemAlertTests(unittest.TestCase):
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)
  
  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)


unittest.main()