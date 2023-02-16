# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 9. User-defined Exceptions

print('''\n
User-defined Exceptions
------------------------- ''')

# So far we have seen how to raise and manage built-in exceptions. In most
# programs, using built-in exceptions won't always be the most detailed way to
# describe an error occuring. What if we could create custom exceptions that are
# more specific to a program or module? Well, Python gives us the abilitiy to create
# user-defined exceptions.
#
# User-defined exceptions are exceptions that we create to allow for better 
# readability in our program's errors. The core syntax looks like this:

class CustomError(Exception):
  pass

# All we have to do to create a custom exception is to derive a subclass from
# the built-in Exception class. Although not required, most custom exceptions
# end in "Error" similar to the naming of the built-in exceptions. We'll learn how
# to customize these exceptions in the next exercise, but for now, let's see how 
# a simple custom exception helps us better document our errors.
#
# Let's imagine that Instrument World has an optional deliver service for
# instruments. If someone tries to schedule a delivery but their address is
# too far, we want to raise a custom LocationTooFarError exception. This
# isn't a type of exception that is built into Python, but rather one that is specific to
# our program and use case. Here is what our program might look like utilizing this
# custom exception:

class LocationTooFarError(Exception):
  pass

def schedule_delivery(distance_from_store):
  if distance_from_store > 10:
    raise LocationTooFarError
  else:
    print('Scheduling the delivery...')

schedule_delivery(9)

# Here, we have a class called LocationTooFarError that inherits from
# the Exception class. By doing so, we are telling Python that we would
# like to be able to use the class as our own custom exception.
#
# Now, if we call schedule_delivery(20), we get the following output:

# Traceback (most recent call last):
#   File "inventory.py", line 10, in <module> schedule_delivery(20)
#   File "inventory.py", line 6, in schedule_delivery
#     raise LocationTooFarError
#     __main__.LocationToFarError

# Since our class name populates into the traceback, even this cimple class proves
# to be more useful than a generic Exception object or any built-in types!
# Users and developers alike will appreciate having specific exception 
# details to work with.
#
# Let's practice creating our own simple custom exceptions!

print('''\n
Tasks
------- ''')

# 1. Instrument World has a program for submitting an online order for an 
#    instrument and then update the inventory. Take some time to look over
#    the current state of the program.
#
#    Can we imagine any specific errors occuring? Run the code to see what
#    happens!
#
# 2. Sometimes we will receive orders that can't be fulfilled because there
#    is not enough inventory for a specific instrument. Let's add some
#    custom exception handling to the program to handle this specific
#    situation.
#
#    Create a class called InventoryError, which inherits from Exception.
#    The body of the class should be a single pass statement
#
# 3. Now, let's deal with the logic of capturing if an exception occurs. Inside
#    of submit_order(), and an if statement after the supply variable is 
#    assigned.
# 
#    The if statement should check if quantity is greater than supply. If it is,
#    then we want to raise our custom InventoryError exception.
#
# 4. Lastly, add an else clause after the if clause, and move the remainder
#    of the function inside of it. This will make sure we execute the rest
#    of the function if the exception is not hit.

class InventoryError(Exception):
  pass

inventory = {
  'Piano': 3,
  'Lute': 1,
  'Sitar': 2
}

def submit_order(instrument, quantity):
  supply = inventory[instrument]
  
  if quantity > supply:
    raise InventoryError
  else:  
    inventory[instrument] -= quantity
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))
  

instrument = 'Piano'
quantity = 5
submit_order(instrument, quantity)
