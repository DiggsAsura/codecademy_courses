# Learn Intermediate Python 3
# 5. Unit Testing
# 2. Unit Testing
# 1. Introduction to Testing

print('''\n
Introduction to (unit) Testing
-------------------------------- ''')

# When working with Python, or any programming language, there is a lot that
# can go wrong with our code. There are syntax errors and exceptions, but 
# there are also mistakes in the program logic which cause it to behave in 
# unexpected ways. 
#
# For these reasons, testing is crucial to creating quality software. The goal
# of testing isn't just to find bugs but to find them quickly. Leaving bugs
# unfound and unresolved can lead to massive consequences in the real world.
# Take a look at some of the most infamous bugs that have ever occured in
# softawre (https://en.wikipedia.org/wiki/List_of_software_bugs)
#
# Don'w worry though - by following some common practices and using the tools
# built into Python, we can start creating quality tests in no time. To dive in,
# first, let's talk about the different types of testing styles that exist.
#
# The world of testing can generally be divided into two categories:
#
# - Manual Testing:
#
#   - With manual testing, a physical person interacts with software much
#     as a user would. In fact, we have been manually testing our code any
#     time we run it and observe the results!
#
# - Automated Testing:
#
#   - With automated testing, tests are performed with code. Generally, automated
#     testing is faster and less prone to human error.
#
# In this lesson, we'll be diving into the world of testing. For most of the
# exercises, let's imagine we've been hired to create tests for a new
# airline company called Small World Air. Before we start writing automated
# tests, let's do some manual testing and see what kind of shape their 
# software is in.
#

print('''\n
Tasks
-------- ''')
# 1. Small World Air provided us access to a program that displays the flight
#    status for all current flights. Manually test the code by running it
#    and observing the output.
#
#



flight_statuses = {
  903: 'Departed',
  834: 'Boarding',
  359: 'Delayed',
  128: 'On time',
  385: 'On time',
}

print('***Small World Air Flight Information***')
for flight, status in flight_statuses.items():
  print('Flight ' + str(flight) + ' status: ' + status)
  
