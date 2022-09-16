# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 11. Expected Failures

print('''\n
Expected Failures
--------------------- ''')

# Sometimes we have a test that we know will fail. This could happen when a 
# feature has a known bug or is designed to fail on purpose. In this case,
# we wouldn't want an expected failure to cloud our test results. Rather than
# simply skipping the test, unittest provides a way to mark tests as expected 
# failures. Expected failures are counted as passed in our test results. If
# the test passes when we expected it to fail, then it is marked as failed
# in test results.
#
# To setup a test to have an expected failure, we can use the expectedFailure
# decorator. Let's consider the following example:

#!import unittest
#!
#!class FeatureTests(unittest.TestCase):
#!  
#!  @unittest.expectedFailure
#!  def test_broken_feature(self):
#!    raise Exception("This test is going to Fail")
#!
#!unittest.main()

# The expectedFailure decorator takes no arguments. The test in the example
# will always fail because an exception was raised during test execution. When
# run, we get the following output:

#!x
#!----------------------------------------------------------------------
#!Ran 1 test in 0.000s
#! 
#!OK (expected failures=1)

# The test failure did not cause any failures in our test results because it
# was marked as expected. Let's do the same for some of our Small World Air
# tests.


print('''\n
Tasks
----------- ''')

# 1. The monitors in front of passenger seats on Small World planes contain a
#    customer feedback portal. The class CustomerFeedbackTests has tests for both
#    the survey and the complaint form.
#
#    We can find the tests in tests.py and the functions that perform feedback
#    tasks in feedback.py. Take some time to get acquainted with the program.
#    Run the code to move on!
#
# 2. Looks like test_survey_form() caught a bug in the customer survey form! It's
#    best not to have this test fail every day while we wait for the bug to get
#    fixed.
#
#    Use the expectedFailure decorator to mark this test as an expected failure!



import unittest
import feedback

class CustomerFeedbackTests(unittest.TestCase):
  
  @unittest.expectedFailure
  def test_survey_form(self):
    self.assertEqual(feedback.issue_survey(), 'Success')
  
  def test_complaint_form(self):
    self.assertEqual(feedback.log_customer_complaint(), 'Success')

unittest.main()