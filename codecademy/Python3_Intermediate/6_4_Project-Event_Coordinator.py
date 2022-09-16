# 6. Iterators & Generators
# 4. Project
# Event Coordinator

# You are staring up your own event coordination business and want to create
# a Python application using generators to help manage your events.
#
# This project will help you practice and further master the use of 
# generators by managing and coordinating customer events for your business.

# Tasks

# 
# Generator Functions & Expressions
#

# 1. You are managing your first customer event! You've been provided a guestlist
#    of names and their ages that are within the file guest_list.txt.
#
#    Within the file script.py, there is a defined function called
#    read_guestlist() that will read in the guestlist file line by line. This
#    function will separate the name and age values and store them into
#    variables named name and age respectively.
#
#    Modify this function to be a generator function that will yield each 
#    read line so that each guest name is yielded each time for the generator.
#
#    Use a for loop, iterate through the generator object that is retrieved by 
#    calling the generator function read_guestlist() and print out the first
#    10 guests on the guestlist.
#
# 2. We've printed out our first 10 guests when our phone rings! It's our
#    customer who has another guest to add to the guestlist.
#
#    She wants to add a guest with the information: "Jane, 35". Use one of 
#    the three generator methods we have learened to accomplish this. 
#
# 3. We can now finish yielding the rest of the names on the guestlist file
#    to our generator by adding numerous next() calls on the generator object
#    until a StopIteration exception is reached. This can also be accomplished
#    by using a for loop on the generator object to automatically make the 
#    appropriate amount of next() calls.
#
# 4. Now that we have all our guests, we want to see which guests are age 21
#    and over so we can inform the bartending vendor.
#
#    Define a generator expression that will use the guests dictionary to 
#    retrieve a generator of names of all guests over 21 years of age.
#
#    We should see our newly added guest, Jane, on the list as well!

#
# Connected Generators & Generator Pipelines
#

# 5. Now it's time to assign meals to each table and the seats at the tables.
#    Our event will have 3 tables with 5 seats at each.
#
#    Create 3 separate generator functions, one for each table, that will
#    yield tuples of ("Food Name", "Table X", "Seat Y") for each of the
#    5 seats at each table.
#
#    You may use the following foods for the tables: Chicken, Beef, Fish.
#
# 6. Finally, we want to assign a table and seat number with meal selection
#    to each guest. Create another generator function that will take in as
#    input our guests dictionary and the connected generator seating/food 
#    selection we created in the previous step. This function should yield a
#    tuple of the guest name and the next value from the connected generator.

#
# Finishing Up
#

# 7. Congratulations, you were able to successfully plan and coordinate your
#    first event!
#
#    Through this project, you were able to reinforce what generators are, how
#    they can be created, manipulated, and connected together to perform
#    complex generator operations.


guests = {}
#Generator Functions
#steps 1-4
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    n = yield name
    if n != None:
      with open(file_name, 'a') as f:
        f.write('\n')
        f.write(n)

#steps 5&6
def table1(Name, Table):
  yield (Name, "Chicken", "Table 1", "Seat {}".format(Table))

def table2(Name, Table):
  yield (Name, "Beef", "Table 2", "Seat {}".format(Table))

def table3(Name, Table):
  yield (Name, "Fish", "Table 2", "Seat {}".format(Table))

def assign_seating(guests):
  counter = 1
  for GSTs in guests:
    if counter < 6:
      yield from table1(GSTs, counter)
      counter += 1
    elif counter < 11:
      N = counter - 5
      yield from table2(GSTs, N)
      counter += 1
    elif counter < 16:
      N = counter - 10
      yield from table3(GSTs, N)
      counter += 1
    else:
      return "No More Seats Available"

#Calling the Functions
#step 1
guest_list = read_guestlist('guest_list.txt')

for i in range(10):
  print(next(guest_list))
#step 2
guest_list.send('Jane,35')
#step 3
for guest in guest_list:
  print(guest)

#step 4
over_21 = (i for i in guests if guests[i] >= 21)

for guest in over_21:
  print(guest + ' is over 21')

#step 5 & 6
assignment = assign_seating(guests)

for seating in assignment:
  print(seating)
  

# Seriously, alot of rambling on the forums too. No hints, no solution. I 
# getting so demotivated by these it took me several days just to go to the
# forum, copy some guys solution and fucking move on. 