# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 12. Review

print('''\n
Review
--------- ''')

# Awesome job! We've covered a lot of material related to unit testing in Python.
# We learned:
#
#   - The difference between manual and automated testing.
#
#   - What unit tests are.
#
#   - How to write simple tests with the assert keyword.
#
#   - How to create and run test cases with the unittest framework.
#
#   - Best practices for test fixtures, test parameterization, skipped tests
#     and expected failures.
#
# The world of software testing is vast and can take time to master, but the 
# basic principles of unit testing will almost always be applicable to any
# language we work with. Incorporating testing into our sofware is the best
# way to prevent unexpected bugs from occuring. The sooner we write tests, 
# the faster we can catch and fix bugs and make our software better!

print('''\n
Tasks
----------- ''')

# 1. The code monitor.py adds some new functionality to the monitor in the 
#    Small World plane seats. Read through it and see what it does. Can you
#    create some unit tests for these functions? Add your tests to 
#    tests.py, and have fun!


import unittest
import monitor

class monitorTestFeature(unittest.TestCase):
  
#  @unittest.expectedFailure
  def test_calculate_remaining_time():
    remaining_time = monitor.calculate_remaining_time()

unittest.main()