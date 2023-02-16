# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 10. Customizing User-defined Exceptions

print('''\n
Customizing User-defined Exceptions
------------------------------------- ''')

# We've just seen how defining a smiple exception class can provide a more
# specific and useful error to users. Defining a simple class is just the first
# step to creating better exceptions in our programs. Python does not stop us from
# customizing our custom exception classes even further.
#
# Let's say we wanted to expand our LocationTooFarError exception from earlier
# to also provide a custom error message. Here is what the custom class
# might look like:

class LocationTooFarError(Exception):
  def __init__(self, distance):
    self.distance = distance
  
  def __str__(self):
    return 'Location is not within 10km: ' + str(self.distance) + 'km'

# Let's break this down:
#
#   - Our class definition doesn't look much different from before. We have
#     a class named LocationTooFarError that still inherits from the built-in
#     Exception class.
#
#   - We have added a constructor that is going to take in a distance argument
#     when we instantiate our exception class. Here, we have overridden the
#     constructor of the Exception class to accept our own custom argument of
#     distance. The reason for taking in a distance is to use it in our
#     __str__ method that will return a custom error message when the
#     exception is hit!
#
#   - The __str__ method provides our exception a custom message by returning
#     a string with the distance property from the constructor.
#
# If we now ran it using our script from earlier:

def schedule_delivery(distance_from_store):
  if distance_from_store > 10:
    raise LocationTooFarError(distance_from_store)
  else:
    print('Scheduling the delivery...')

schedule_delivery(9)
# We would see our expanded custom exception in action:

# Tracebacok (most recent call last):
#   File "inventory.py", line 14, in <module> schedule_delivery(20)
#   File "inventory.py", line 11, in schedule_delivery
#     raise LocationTooFarError(distance_from_store)
#     __main__.LocationTooFarError:
#       Location is not within 10 km: 20

# Let's practice customizing our exception even further!



print('''\n
Tasks 
------ ''')
# 1. Let's customize the InventoryError from our previous exercise to return a
#    custom error message. Inside the class, replace the pass statement with an
#    __init__ method which takes two arguments, self and supply
#
#    Inside the method, store suply into the variable self.supply
#
#

class InventoryError(Exception):
  def __init__(self, supply):
    self.supply = supply
  
  def __str__(self):
    return 'Available supply is only ' + str(self.supply)

inventory = {
  'Piano': 3, 
  'Lute': 1, 
  'Sitar': 2
}

def submit_order(instrument, quantity):
  supply = inventory[instrument]

  if quantity > supply:
    raise InventoryError(supply)
  else:
    print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))
  
instrument = 'Piano'
quantity = 5

submit_order(instrument, quantity)

# Everything makes sense, but the __str__ method. I probably need to read up
# more on this one isolated. I thought it would be a matter of __repr__
# but yea nope..