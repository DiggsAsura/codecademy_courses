# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 8. The finally Clause

print("""\n
The finally Clause
-------------------- """)

# With try/except/else, we've seen how to run certain code when an exception
# occurs and other code when it does not. There is also a way to execute
# code regardless of wheter an exception occurs - the finally clause.
#
# Here is our final flow char emonstrating try/except/else/finally:

#
#                               Start
#                                 |
#                              Execute
#                            try clause
# Execute                         |                     Execute
#  except  <-- Yes <-- Exception encountered --> No --> else 
#  clause                                               clause
#    |                         Execute                    |
#    |-----------------------> Finally <------------------|
#                               clause
#                                 |
#                                End
#

# Let's return to our fictional login program from earlier and examine a use case
# for the finally clause:

#try:
#  check_password()
#except ValueError:
#  print('Wrong Password! Try again!')
#else:
#  login_user()
#finally:
#  load_footer()

# In the above program, most of our code stayed the same. The one change we 
# made was we added the finally clause to execute no matter if the user fails
# to login or not. In either case, we use an imaginary function called load_footer()
# to load the page's footer. Since the footer area of our imaginary application
# stays the same for both states, we always want to load it, and thus call it
# inside of the finally clause.
#
# Note that the finally clause can be used independently (without an except or
# else clause). This is convenient way to guarantee that behavior will occur,
# regardless of wheter an exception occurs:

#try:
#  check_password()
#finally:
#  load_footer()

# Let's put the finally clause into practice for our Instrument World 
# application!

print("""\n
Tasks
---------- """)

# 1. Instrument World maintains a database (in this case a large dictionary)
#    with instrument information that any store can access.
#
#    The current program displays information from the database for a particular
#    instrument. Take some time to look over database.py and instrument.py to
#    get better acquainted with the program.
#
#    Run the code to examine the output!
#
# 2. Since the database server Instrument World uses can only have a limited 
#    number of users connected to it, we want to make sure that we disconnect
#    from it after attempting to retrieve information, even if an 
#    exception occurs.
#
#    Add a finally clause that calls database.disconnect_from_database(). 
#    Observe the output of the exception handling when we hit an 
#    exception by running the code!
#
# 3. Change instrument to have a value of 'Kora'. Run the code to observe
#    the finally clause executing even when we don't hit an exception.

import database

instrument = 'Kora'
database.connect_to_database()

try:
  database.display_instrument_info(instrument)
except KeyError:
  print('Oh no! This instrument does not exist.')
else:
  print(instrument)
finally:
  database.disconnect_from_database()