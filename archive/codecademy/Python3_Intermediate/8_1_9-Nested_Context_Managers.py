# 8. Resource Management
# 1. Context Managers
# 9. Nested Context Managers

print('\nNested Context Managers\n')

# So far, we've only been using context managers within the context (Ha! Get it?)
# of one file. In most programs, there might be a need to use context managers for 
# a couple of different scenarios that include working with multiple files! For 
# example, we might want to:
#
# - Work with information from multiple files.
#
# - Copy the same information to multiple files. 
#
# - Copy information from one file to another.
#
# To accomplish this goal of working with multiple resources at once, context
# managers can be nested together in a with statement to mange multiple
# resources simultaneously.
#
# Let's imagine we have two files: a teacher.txt file and a student.txt. We 
# want to copy all the information on the student file to the teachers. Our code
# might look like this:

with open('teacher.txt', 'a') as teacher, open('student.txt', 'r') as student:
  teacher.write(student.read())

# Notice:
#
# - The with statement is being called once but invoking two context managers.
#   This is a single-line nested with statement.
#
# - Each context manager is separated by a comma and has its own target variable.
#
# - Our teacher.txt file is being opened in write mode because it will be written
#   into (actually, I changed mine to 'a') and our student.txt is opened in read
#   mode because we are attempting to copy the text into the teacher's file.
#
# - The resulting teacher.txt file will now include everything that was in the
#   student.txt file (actually, replaced it entirely...) 
#
# - Here we have chosen to use the open() built-in function rather than a custom
#   context manager. It is entirely possible to use our own in place of the open()
#   function.
#
# We can also write the above nested context managers in a slightly different way:

with open('teacher.txt', 'a') as teacher:
  with open('student.txt', 'r') as student:
    teacher.write(student.read())

# Notice that this syntax is almost similar to the first method. However, here are
# some differences to note:
#
# - The with statement is being called twice
#
# - The with statement statement to open student.txt is read mode is nested
#   in the code block of the with statement that opens teacher.txt in
#   write mode.
#
# - This method, through slightly longer gives a clearer visual of nesting and is
#   preferable when working with more than two context managers.
#
# Let's practice nesting context managers with our poem_files decorator-based
# context manager from earlier!


print('\nTasks\n')

# 1. Let's return to our poem context manager. This time, we want to start 
#    transferring poems from a poem.txt file to a card.txt file. We plan to 
#    create some poem greeting cards for all our friends!
#
#    Write a nested context manager that uses the poem_files context manager to
#    open poem.txt in read mode and saves it to a variable called poem
#
#    Nested inside, use the card_files context manager to open the card.txt file
#    in write mode and saves it to a variable called card. 
#
#    Print poem and card to confirm we can access both files. 
#
# 2. Finally, inside of our nested context managers, and under our print
#    statements, write to card.txt the contents of poem.txt

from contextlib import contextmanager

@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = file.open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()

@contextmanager
def card_files(file, mode):
  print('Opening File')
  open_card_file = open(file, mode)
  try:
    yield open_card_file
  finally:
    print('Closing File')
    open_card_file.close()


with open('card.txt', 'w') as card, open('poem.txt', 'r') as poem:
  card.write(poem.read())