# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 2. The assert Statement

print('''\n
The assert Statement
---------------------- ''')

# While the previous example was simple to test, most code will be much more 
# complex. It would be very tedious to have to perform these tests manually.
# Our time would be better spent writing automated tests.
#
# Luckily, Python provides an easy way to perform simple tests in our code -
# the assert statement. An assert statement can be used to test that a 
# condidtion is met. If the condition evaluates to False, an AssertionError
# is raised with an optional error message.
#
# The general syntax looks like this:
#! assert <condition>, 'Message if condition is not met'
#
# Consider the following example that demonstrates the assert statement 
# paired with a function called times_ten. Note there is a bug in the fucntion
# for demonstration purposes.

def times_ten(number):
  return number * 100

result = times_ten(2) # 20, but fixed to let the code run
assert result == 200, 'Expected times_ten(20) to return 200, instead got ' + str(result)

# Here, we want to test if our times_ten() function works as intended. We 
# use the assert statement to evaluate the expression result == 200 since
# we expect that our function would return 200 given an input of 20. Since
# this is not the case, this expression evaluates to False (there is a bug in
# times_ten() - it acually multiplies by 100!), we get the following
# exception:

#! AssertionError: Expected times_ten(20) to reuturn 200, instead got 2000

# An assert statement is a quick and powerful way to verify that a program is
# in the correct state. They can be used to catch mistakes early and make sure we
# avoid any catastrophes. Let's practice using assert to get a feel for 
# automated testing!

print('''\n
Tasks 
------- ''')
# 1. Small World Air has a program that runs at the check-in kiosk and asks 
#    passengers for their destination airport code.
#
#    Currently, Small World only flies to three destinations: Budapest (BUD),
#    Casablanca (CMN), and Istanbul (IST). Take some time to examine the
#    program.
#
#    What should the program return for the current set destination of 
#    'HND' (an airport in Tokyo, Japan)?
#
# 2. This error wasn't a very userfiendly experience! We also want to make sure
#    that users are not entering destinations that Small Air World does not
#    travel to. Let's add an automated test using assert!
#
#    Add an assert statement that checks if destination is in the destinations
#    keys. If it isn't, the AssertionError message should read, 'Sorry, Small
#    World currently does not fly to this destination!'



destinations = {
  'BUD': 'Budapest',
  'CMN': 'Casablanca',
  'IST': 'Istanbul'
}

print('Welcome to Small World Airlines!')
print('What is the airport code of your travel destination?')
destination = 'HND'

assert destination in destinations, 'Sorry, Small World currently does not fly to this destination'

city_name = destinations[destination]
print('Great! Retrieving information for your flight to ....' + city_name)


# Ok the assert syntax got me. I tried assert destination not in, but it turns
# out it should just be destination in destinations.

