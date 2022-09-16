# Learn Intermediate Python 3
# 5. Unit Testing
# 1. Exceptions
# 7. The else Clause

print("""\n 
The else Clause
-----------------""")
# We've seen how exception handlers get executed when we encounter exceptions
# durint a try clause- but what if we want to run some code only if we do not
# encounter an exception? Python provides us a way to do this as well - the 
# else clause.
#
# Our updated flow chart shows what happens when an else clause is added
# to the mix:


#                                         Start
#                                           |
#                                  Execute try clause
#                                           |
# Execute except clause <- Yes <--Execption encountered--> Execute else clause
#           |                                                        |
#           |----------------------------> End <---------------------|


# Python will only execute the else clause if no exception was encountered in 
# the try clause.
#
# Let's examine a hypothetical program that authenticates a user. For now, we
# will use two imaginary functions check_password() and login_user().
# Here is what the program looks like:

def check_password(password):
  if password == 'correct_password':
    print("ok!")
def login_user():
  print("Logged in")

try:
  check_password("correct_password")
except ValueError:
  print('Wrong Password! Try again!')
else:
  login_user()

# In this program, we can assume if our function check_password() fails, it will
# return a ValueError. Thankfully, our exception handler takes care of this 
# scenaroi. However, if our function doesn't fail, the else clause allows us to 
# log the user in!
#
# Now, one could argue, we could have written our program a different way to
# achieve a similar outcome:

#try:
#  check_password()
#  login_user()
#except ValueError:
#  print('Wrong Password! Try again!')

# Here, if our check_password() ever fails, we will be able to catch the execption
# just like before. Python does offer a bit of insight on this scenario in the 
# official documentation:
#
#   The use of the else clause is better
#   than adding additional code to the 
#   try clause because it avoids
#   accidentally catching an exception
#   that wasn't raised by the code being
#   protected by the try ... except
#   statement
#
# This suggestion is valid in this case since in the alternative style, the ValueError
# could occur in any of the other lines of code other than check_password(), and
# it would be challenging to tell where it came from.
#
# Let's give the else clause a try!

print("""\n
Tasks
------- """)

# 1. Our Instrument World stores have a customer rewards program. Examine
#    the code which displays a customer's account number. Spot any
#    issues? Run the code to find out!
#
# 2. Looks like our pesky KeyError is back! Let's try to account for this
#    scenario by using exception handling.
#
#    Wrap rewards_number = customer_rewards[customer] inside of a 
#    try clause. Add an except clause which catches a KeyError and
#    prints 'Customer was not found in rewards program!'.
#
# 3. Lastly, add an else clause and move print('Rewards account number is:
#    ' + str(rewards_number)) so that it is inside of the else clause.
#
# 4. Change the value of the customer variable so that it is equal to 'Mario'.
#
#    What we should expect from our output given our new exception handling
#    structure? Ponder the question and then run the code to find out!

customer_rewards = {
  'Zoltan': 82570,
  'Guadalupe': 29850,
  'Mario': 17849
}

def display_rewards_account(customer):
  try:
    rewards_number = customer_rewards[customer]
  except KeyError:
    print('Customer was not found in rewards program!')
  else:
    print('Rewards account number is: ' + str(rewards_number))


customer = 'Zuigly'
customer2 = 'Mario'
display_rewards_account(customer)
display_rewards_account(customer2)