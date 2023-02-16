# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 3. Raising Exceptions

# Fuck it, i'm not sure if theres a point of writing out the whole god dam
# chapter. I mean, i did because I was thinking it might make things stick better
# but I'm really not sure. I try for a while without doing it. 

# Examples on raising a NameError
#raise NameError
#raise NameError('Custom Message')

# Example on raising a TypeError
def open_registry(employee_status):
  employee_status == 'Authorized'
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    # Alternatives: Raise TypeError() or TypeError("Message")
    raise TypeError("Nope")
#open_registry("Kenneth")

# Another example where we use the base Exception class and provide a single
# argument that serves as the error message. 

def open_register2(employee_status):
  employee_status != 'Authorized'
  if employee_status == 'Authorized':
    print('Successfully opened cash register')
  else:
    raise Exception('Employee does not have access!')
#open_register2('Kenneth')

#! As a rule of thumb, use an exception that provides the best explanation for the
# !expected error for both the user and anyone that will read the code.


# Task

instrument_catalog = {
  'Marimba': 1999,
  'Kora': 499,
  'Flute': 899
}

def print_instrument_price(instrument):
  # Write your code below:
  if instrument in instrument_catalog:
    print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
  else:
    raise KeyError(instrument + ' not in the instrument catalog!')

print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')