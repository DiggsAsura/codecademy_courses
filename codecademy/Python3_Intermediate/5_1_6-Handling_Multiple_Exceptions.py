# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 6. Handling Multiple Exceptions

print("""\n
Handling Multiple Exceptions 
------------------------------ """)

# While handling a single exception is useful, Python also gives us the ability to
# handle multiple exceptions at once. We can list more than one exception type in a
# tuple with a single except clause. Here is what the syntax would look like:

try:
  print(1 + a)
except (NameError, ZeroDivisionError) as e:
  print('We hit an exception!')
  print(e)

# In the above example, we expect to encounter either a NameError or a
# ZeroDivisionError. We can list any number of exceptions in the tuple format
# as long as it makes sense for the code in our try block. This is where we can
# see the benefit of capturing our exception object (via the as clause) since it 
# enables us to print (or operate on) the specific exception that is caught.
#
# In addition to catching multiple exceptions, we can also pair multiple except
# clauses with a single try clause, enabling specific exceptions to be handled
# differently. For example:

try:
  print(1 + a)
except NameError:
  print("We hit a NameError Exception!")
except KeyError:
  print("We hit a TypeError Exception")
except Exception:
  print("We hit an exception that is not a NameError or TypeError")
  
# In the above program, a NameError or KeyError will trigger one of the first two
# exception handlers. Any other exception will trigger the third handler. Any other
# exception will trigger the third handler. Note that the order of handlers is 
# important here - if an exception is encountered, Python will execute the first 
# one that matches its type. In this case, and a valid strategy for exception handling,
# we use the last except clause as a generic Exception as a backup if no other
# specific exception gets caught.
#
# Let's now practice handling multiple exceptions!

###
print("""\n
Tasks 
------- """)

# 1. Instrument World has a program that allows the user to apply a discount to an
#    instrument price.
#
#    Take some time to look over the program. Spot any issues? Run the code to 
#    to find out!
#
# 2. Looks like we hit a KeyError! Let's apply some exception handling to handle
#    this exception!
#
#    Wrap the display_discounted_price() function call in a try clause. In addition,
#    add an except clause which handles a KeyError exception. Inside the execpt
#    clause, print 'An invalid instrument was entered!'
#
# 3. Awesome! Now our program can account for any KeyError we encounter. Let's see 
#    what happens when we use a key that does exist in our instrument_prices dictionary.
#
#    Change instrument = 'Clarinet' so that instrument is equal to 'Banjo'. Before
#    you run the code, take some time to ponder if our program will run into any error.
#
# 4. We hit a TypeError !
#
#    This happened because the discount variablewas set to a string, not a number.
#    Let's adjust our exception handling to also account for a TypeError.
#
#    After the exception handler for KeyError, add another except clause which
#    catches a TypeError. Inside the except clause, print 'Discount percentage
#    must be a number!'
#
# 5. We now have exception handlers for when we hit a KeyError or TypeError,
#    but what if some other unexpected exception occurs?
#
#    Add a final exception handler which will catch any Exception object. Inside,
#    print 'Hit an exception other than KeyError or TypeError!'

instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted priec is " + str(discounted_price))
  
instrument = 'Banjo'
discount = '20'

try:
  display_discounted_price(instrument, discount)
except KeyError:
  print('An invalid instrument was entered')
except TypeError:
  print('Discount percentage must be a number')
except Exception:
  print('Hit an exception other than KeyError or TypeError!')