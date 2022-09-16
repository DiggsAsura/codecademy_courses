# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 4. Try / Except

print("""\n
Exceptions
Try / Except
---------------""")

# So far, the exceptions we've encountered have caused our programs to stop 
# executing. However, it is possible for programs to continue executing even
# after encountering an exception. This process is known as exception handling
# and is accomplished using the Python try / except clauses.
#
# The following flow chart demonstrates the mecahnics of try/except:

#   Start
#    |
#   Execute try clause
#    |
#   Exception encountered   -> Yes -> Execute execpt clause
#    |                                       |
#    No <------------------------------------
#    |
#   End

# Let's break it down:
#
#   - Python will first attempt to execute code inside the try clause code block.
#
#   - If no exception is encountered in the code, the except clause is skipped
#     and the program continues normally.
#
#   - If an exception does occur inside the try code block, Python will immediately
#     stop executing the code and begin executing the code inside the except code 
#     block (sometimes called a handler).
#
# Let's see this in action in a small program that prints colors:

colors = {
  'red': '#FF0000',
  'blue': '#0000FF',
  'yellow': '#FFFF00'
}

for color in ('red', 'green', 'yellow'):
  try:
    print('The hex value of ' + color + ' is ' + colors[color])
  except:
    print('An exeption occured! Color does not exist.')
    print('Loop continues...')

# We get the following output:
# The hex value of red is #FF0000
# An exception occured! Color does not exist.
# Loop continues...
# The hex value of yellow is #FFFF00

# In the above code, the try block runs until it hit an exception. The hex
# value of the color red was successfully printed before it tried to access the
# hex value of green, which caused a KeyError since green is not in our colors
# dictionary and ran the code in the except block.
# However, the exception was handled so Python continued executing our code
# and went onto print the hex value of yellow.
#
# Exception handling is a powerful tool that lets us gain more flexibility in
# dealing with errors in our applications. We can use it to perform an action
# multiple times until it succeeds, or perhaps simply print a message when a 
# non-critical part of our program doesn't work properly.
#
# Let's try performing some exception handling!
#


print("""\n
Tasks
------- """)

# 1. Instrument World has a program that prints a staff report for all of the 
#    Instrument World locations in the staff dictionary.
#
#    Take some time to review the code. Spot any issues?
#
# 2. We successfully printed the staff report for Austin, but we hit an exception
#    (ZeroDivisionError) when trying to print out the ratio for Melbourne since
#    we attempted to divide 8 by 0.
#
#    Let's use exception handling to manage this error and keep our program 
#    running. First, wrap the function call print_staff_report() in a try clause.
#
# 3. Immediately after the try clause, add an except clause which prints
#    'Could not print sales report for ' + location
#
#    Run the code and observe our exception handling!

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
  }
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
  except:
    print('Could not print sales report for ' + location)
