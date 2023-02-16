# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 5. Catching Specific Exceptions

print("""\n
Exceptions
Catching Specific Exceptions
----------------------------- """)

# The exception handlers from the previous exercise handled any exception hit during
# the try clause. However, in most cases, we will have an idea of the types of 
# exceptions that might occur within our code. It is generally considered best
# practice to be as specific as possible with the exceptions we want to raise unless
# there is a specific reason for catching any type of exception.
#
# We can catch a specific exception by listing it after the except keyword, as
# in the example below:

try:
  print(undefined_var)
except NameError:
  print('We hit a NameError')

# In this case, the except block is only executed if a NameError is encountered
# (in the try block) rather than any exception. If any other exception occurs,
# it is unhandled, and the program terminates.
#
# When we specify exception types, Python also allows us to capture the exception
# object using the as keyword. The exception object hosts information about
# the specific error that occured. Examine our previous function but now capturing
# the exception objec as errorObject:

try:
  print(undefined_var)
except NameError as errorObject:
  print('We hit a NameError')
  print(errorObject)

# Output:
# We hit a NameError
# name 'undefined_var' is not defined

# Its worth noting errorObject is an arbitrary name and can be replaced with
# any name we see fit. The following code would work exactly the same:

try:
  print(undefined_var)
except NameError as e:
  print('We hit a NameError')
  print(e)
  
# Let's get some practice capturing specific exceptions.

#############
print("""\n
Tasks
-------""")
# 1. Let's improve upon the exception handler we built in the previous exercise.
#
#    Change the except clause so that it only handles a ZeroDivisionError. Store
#    the ZeroDivisionError we intend to capture into a variable called e.
#
# 2. Print e as the second print() statement in the except block.

staff = {
  'Austin': {
    'floor managers': 1,
    'sales associates': 5
  },
  'Melbourne': {
    'floor managers': 0,
    'sales associates': 8
  },
  'Beijing': {
    'floor managers': 2,
    'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  try:
      print_staff_report(location, staff)
  # Write your code below:
  except ZeroDivisionError as e:
      print('Could not print sales report for ' + location)
      print(e)
