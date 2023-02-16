# 6. Iterators & Generators
# 3. Generators
# 5. Generator Methods: send()

from tkinter import N


print('\nGenerator Methods: send()\n')

# Python provides a few special methods to manipulate generators!
#
# The .send() method allows us to send a value to a generator using the yield
# expression. If you assign yield to a variable the argument passed to the
# .send() method will be assigned to that variable. Calling .send() will
# also cause the generator to perform an iteration.
#
# Look at the following example to see the behavior of the .send() method:

def count_generator():
  while True:
    n = yield
    print(n)

my_generator = count_generator()
next(my_generator) # 1st Iteration Output:
next(my_generator) # 2nd Iteration Output: None
my_generator.send(3) # 3rd Iteration Ouput: 3
next(my_generator) # 4th Iteration Output: None

# In the code example above, the generator definition contains the line 
# n = yield. This assigns the value in yield to n which will be None unless
# a value is passed using .send().
#
# The last 4 lines in the code are 4 iterations, 3 using next() and one using
# the .send() method:
#
#   - The 1st iteration creates no output since the execution stops at 
#     n = yield which is before print(n).
#
#   - The 2nd iteration assigns None to n through the n = yield expression.
#     None is printed.
#
#   - The 3rd iteration is caused by my_generator.send(3). The value 3 is
#     passed through yield and assigned to n. 3 is printed.
#
#   - The last, and 4th, iteration, assigns None to n. None is printed.
#
# The .send() method can control the value of the generator when a second
# variable is introduced. One variable holds the iteration value and the 
# other holds the value passed through yield.

print('\n --- \n')
def generator():
  count = 0
  while True:
    n = yield count
    if n is not None:
      count = n
    count += 1

my_generator2 = generator()
print(next(my_generator2)) # Output: 0
print(next(my_generator2)) # Output: 1
print(my_generator2.send(3)) # Output: 4
print(next(my_generator2)) # Output: 5

# In the above example, the generator functoin defines count = 0 as the iteration
# value. n is used to hold the value provided by yield. Just like next(), the
# .send() method returns the value of the recent iteration. In this example,
# the return values are printed using print().
#
# The updated line, n = yield count, has 2 behaviors:
#
#   - At the start of each iteration the value provided by yield is assigned
#     to n. This value will be None when next() causes an iteration or it will
#     be equal to the value passed using .send()
#
#   - At the end of each iteration, the value stored in count is returned 
#     by the generator.
#
# If n is not None, the value stored in n can be assigned to the iterator variable,
# count. This allows the iterator to only change the value of count when the
# .send() method is called.

print('\n --- ')
print('Tasks\n')

# 1. You are a teacher with a roster of 50 students. You have created a generator,
#    get_student_ids(), that outputs each student's id which you then use
#    for assignment grading.
#
#    Things to note about the code in the workspace:
#
#     - MAX_STUDENTS is set to 50 and is used in the while loop condition to 
#       cutoff the iteration.
#
#     - student_id is initialized to 1 and is incremented at the bottom of
#       the while loop.
#
#     - The generator currently uses yield to return student_id at the end
#       of each iteration.
#
#     - A for loop at the bottom of the code iterates through the generator
#       object student_id_generator and outputs each id.
#
#    Run the code to see all 50 ids printed.
#
# 2. When you are interrupted while grading, you need to pick up where you 
#    left off! This requires you to start the id generation at a number 
#    higher than 1. One way to solve this problem is to change the generator
#    to support the .send() method.
#
#    Inside get_student_ids():
#
#     - Change the yield expression so the value from yield is assigned to n.
#
#     - Just below the yield expression check that n is not equal to None. If
#       they are not equal, assign the value of n to student_id.
#
#     - Still inside the if statement, stop student_id from incrementing by 
#       skipping the rest of the iteration.
#
#    When you run the code, you should see no change.
#
# 3. To start the iteration at a different id, you want to send the generator
#    a new value during the first iteration.
#
#    Inside the for loop and before print(i):
#
#     - Check if i is equal to the first id number, 1.
#
#     - If so, set i to return value of the student_id_generator.send() method.
#
#     - Set the argument for the .send() method so that the output start
#       at 25.


MAX_STUDENTS = 50

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    n = yield student_id
    if n is not None:
      student_id = n
      continue
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  if i == 1:
    i = student_id_generator.send(25)
  
  print(i)