# Learn Intermediate Python 3
# 1. Function Arguments
# 2. Function Arguments
# 3. Working with *args

# Now that we have seen the basics of working with positional argument unpacking
# let's examine how to use it in a more meaningful way.
#
# Say we wanted to build a function that works similarly to our trusty print()
# statement but instead prints all of the arguments in uppercase form. Using
# our knowledge of iteration, combined with the power of the unpacking operator, 
# our solution might look like this:
def shout_strings(*args):
  for argument in args:
    print(argument.upper())
#
shout_strings("Working on", "learning", "argument unpacking!")
#
# Would output:
# WORKING ON
# LEARING
# ARGUMENT UNPACKING!
#
# In our function shout_strings(), we use a for loop (although we could use any
# iterator) to iterate through each element of the tuple that exists inside of args.
# Then we use the built-in function .upper() to capitalize each argument. 
#
# The unpacking operator is not limited to being used alone, but rather it can be
# combined with other positional arguments. Let's examine a function that truncates 
# (cuts off) sentences based on provided length:
def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])
#
truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
#
# Would output:
# What's g
# Looks li
# 
# Let's break this down:
#   - We have two parameters that our function truncate_sentences() defines. The first
#     is a length parameter that will specify how many characters we want to keep.
#     The second is a parameter called sentences that is paired with the unpacking
#     operator, signifying it will take a variable number of arguments.
#   
#   - On each iteration of the function, we are looping through the tuple created by
#     the sentences argument (because it is paired with the unpacking operator) and 
#     perform a slice on the sentence based on the provided length argument. This
#     forces every value in the sentences tuple to be cut down in length.
#
# Utilizing iteration and other positional arguments are two common ways we can 
# increase the utility of our functions when using the unpacking operator (*). Let's
# practice using these techniques to see how powerful they are!
#

# Tasks
# 1. Jiho is having a lot of success with our resturant application. Unfortunately,
#    our original design did not account for storing orders for each specific table.
#    Jiho asked us to adjust our application to be able to store the orders that
#    that come in for each specific table and also be able to print out the order for
#    for the kitchen staff.
#
#    Take some time to review the adjusted structure of the program we created earlier.
#    Note that tables is now a dictionary with the table numbers as the keys. It also 
#    accounts for a new property called order. The assign_table function has also been 
#    adjusted to account for the changes.
#
#    Run the code to move onto the next checkpoint.
#
# 2. To help Jiho implement the ability to store the order in a specific table, let's
#    implement a function called assign_and_print_order().
# 
#    The function should have two parameters called table_number and order_items. The
#    parameter of order_items should be grouped with an unpacking operator (*) so 
#    we can capture a variable number of order items per table.
#
#    For now, our program will error out if we run it. Don't worry we fill fill in the 
#    function in the next step!
#
# 3. Our function assign_and_print_order() should then assign an order to a table. 
#    Inside of our function access the nested order key for the specific table (using
#    the table_number argument) from tables and set it to the order_items parameter.
#
# 4. In addition to assign the order to our tables dictionary, we also want to print
#    every ordered item so the kitchen knows what to cook!
#
#    Inside of assign_and_print_order() use a for loop to iterate through order_items
#    and print each individual order item.
#
# 5. Lastly, let's see our function in action. Luckily we just had a new customer 
#    come in for their reservation. Use the assign_table() function to add a new 
#    customer named 'Arwa' to table 2 with a VIP status set to True.
#
# 6. Now that Arwa is seated and ready to order, call our assign_and_print_order()
#    function for table 2 with the order of 'Steak', 'Seabass', and 'Wine Bottle'.
# 
#    Print tables and see the result!


tables = {
  1: {'name': 'Jiho', 'vip_status': False, 'order': 'Orange Juice, Apple Juice'},
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {}
}
print(tables)

def assign_table(table_number, name, vip_status=False):
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

# Wow nice. I like how this Intermediate lay it out. It's incredibly difficult to wrap
# my head all yet, but I really like how they show how it will look, before we go 
# on to how we do it. GG whoever made these chapters at Codecademy.

def assign_and_print_order(table_number, *order_items):
  # This one i had to look at solution. I somewhat was close, but I don't understand ['order']
  tables[table_number]['order'] = order_items
  for order in order_items:
    print(order)
  
assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')

print(tables)


# While I still scratch my head a fair bit, lol, I still really enjoy it. I think some stick :D