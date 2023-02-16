# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 9. Test Fixtures

import unittest


print('''\n
Test Fixtures
----------------- ''')

# One of the most important principles of testing is that tests need to occur in a
# known state. If the conditions in which a test runs are not controlled, then our
# results could contain false negatives (invalid failed results) or false positives
# (invalid passed results).
#
# This is where test fixtures come in. A test fixture is a mechanism for ensuring
# proper test setup (putting tests into a known state) and test teardown
# (restoring the state prior to the test running). Test fixtures guarantee that our
# tests are running in predictable condidtions, and thus the results are reliable.
#
# Let's say we are testing a Bluetooth device. The device's Bluetooth module
# can sometimes fail. When this happens, the device needs to be power cycled
# (shut off and then on) to restore Bluetooth functionality. We would not
# want tests to run if the device was already in a failed state because these
# results would not be valid. Furthermore, if our tests cause the Bluetooth
# module to fail, we want to restore it to a working state after each test.
# Here is how we might do it:

#!import unittest
#!
#!def power_cycle_device():
#!  print('Power cycling bluetooth device...')
#! 
#!class BluetoothDeviceTests(unittest.TestCase):
#!  def setUp(self):
#!    power_cycle_device()
#! 
#!  def test_feature_a(self):
#!    print('Testing Feature A')
#! 
#!  def test_feature_b(self):
#!    print('Testing Feature B')
#! 
#!  def tearDown(self):
#!    power_cycle_device()
#!
#!unittest.main()

# The unittest framework automatically identifies setup and teardown methods
# based on their names. A method named setUp runs before each test case in the
# class. Similarly, a method named tearDown gets called after each test case.
# Now, we can guarnatee that our Bluetooth module is in a working state before
# and after every test. Here is the output when these tests are run:

#!Power cycling bluetooth device...
#!Testing Feature A
#!Power cycling bluetooth device...
#!.Power cycling bluetooth device...
#!Testing Feature B
#!Power cycling bluetooth device...
#!.
#!----------------------------------------------------------------------
#!Ran 2 tests in 0.000s
#! 
#!OK
    
# Let's consider another scenario. Perhaps our tests rely on working Bluetooth, but
# there is nothing in the tests that would cause the bluetooth to stop working. In
# this case, it would be inefficient to power cycle the device before and after every
# test. Let's refactor the previous example so that setup and teardown only
# happen once - before and after all tests in the class are run:

#!import unittest
#!
#!def power_cycle_device():
#!  print('Power cyclling bluetooth device...')
#!
#!class BluetoothDeviceTests(unittest.TestCase):
#!  @classmethod
#!  def setUpClass(cls):
#!    power_cycle_device()
#! 
#!  def test_feature_a(self):
#!    print('Testing Feature A')
#!  
#!  def test_feature_b(self):
#!    print('Testing Feature B')
#!  
#!  @classmethod
#!  def tearDownClass(cls):
#!    power_cycle_device()
#!    
#!unittest.main()

# We replaced our setUp method with the setUpClass method added @classmethod
# decorator. We changed the argument self to cls because this is a class method.
# Similarly, we replaced the tearDown method with the tearDownClass class method.
# Now, we get the following output:

#!Power cycling bluetooth device...
#!Testing Feature A
#!Testing Feature B
#!Power cycling bluetooth device...
#! 
#!----------------------------------------------------------------------
#!Ran 2 tests in 0.000s
#! 
#!OK

# In addition to calling functions, we can also use setup methods to instantiate
# objects and or gather any other data needed. Anything stored in our class will
# be available throughout our test function.
#
# It's generally good practice to create fixtures that run for every test. However,
# when a fixture has a large cost (i.e. it takes a long time), then it might make
# more sense to have it run once per test class rather than once per test. Let's
# practice setting up test fixtures!


print('''\n
Tasks
-------------- ''')

# 1. In our tests.py file we have some simple tests written for the passenger 
#    check-in experience at the kiosk for Small World Air. We also have some
#    functions we are testing writtin in kiosk.py.
#
#    Take some time to review the provided code in both files. Run the code
#    to continue!
#
# 2. We want to make sure the kiosk is powered on before we run any tests.
#    This is a great time to setup some test fixtures!
#
#    Create a setUpClass() method which takes a single argument (cls) and
#    calls kiosk.power_on_kiosk(). Add the @classmethod decorator on
#    top of it!
#
# 3. We don't want to leave the kiosk powered on after all tests are run.
#
#    Create a tearDownClass() method which takes a single argument (cls) and
#    calls kiosk.power_off_kiosk(). Add the @classmethod decorator on 
#    top of it!
#
# 4. We also want to make sure that customers are on the welcome page before each
#    test runs. Create a method called setup(). Inside of the method, call
#    kiosk.return_to_welcome_page()


import unittest
import kiosk

class CheckInKioskTests(unittest.TestCase):

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  # Write your code below:
  @classmethod
  def setUpClass(cls):
    kiosk.power_on_kiosk()
  
  @classmethod
  def tearDownClass(cls):
    kiosk.power_off_kiosk()
  
  def setUp(self):
    kiosk.return_to_welcome_page()

unittest.main()

# Ok I'm falling off a bit, this is very very dry. 