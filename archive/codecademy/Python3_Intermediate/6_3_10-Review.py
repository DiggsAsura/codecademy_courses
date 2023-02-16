# 6. Iterators & Generators
# 3. Generators
# 10. Review

print('\nReview -----')

# Congratulations! You have completed the Generators lesson! In this lesson,
# you learned how to:
#
#   - Create generator functions using yield
#
#   - Implement generator expressions
#
#   - Use built-in generator methods like .send(), .throw() and .close()
#
#   - Connect generators into single generators
#
#   - Use nested or piplined generators
#
# Let's review these topics one final time.

print('\Tasks -----')

# 1. Create a generator function called graduation_countdown() that will 
#    countdown the number of days left before student graduation. It should
#    take in as input days and yield one less day on each next() call until
#    0 is reached. Use a while loop for yielding and decrementing the day.
#
# 2. Create an equivalent generator expression called countdown_generator for
#    the graduation_countdown generator function. It should generate the 
#    days in a descending order starting from the provided days value. Place
#    the code after the days = 25 line.
#
# 3. Modify the graduation_countdown() generator function to accept values 
#    sent using send(). Use a local variable called days_left to store
#    sent values. Use an if/else statement to check for sent values.
#
# 4. Call the graduation_countdown() function and set it to a variable 
#    called grad_days.
#
#    Iterate through grad_days generator to print the number of days left
#    with a string of "Days Left: x" where x represents the countdown value.
#
#    On the 15th day of the graduation countdown, the school president
#    announcens that the graduation will be moved up 5 days. Send a value of
#    10 to the grad_days generator when the 15th day in the countdown is
#    reached.
#
# 5. It's our lucky day! The school president announces that graduation will 
#    now occur on the 3rd day left of the countdown. Modify the for loop so 
#    that when the countdown is 3, the generator will close. Insert the 
#    condition check and close() before "Days Left" printout.
#
# 6. We have three honors achievements to assign to students that are defined
#    within the summa(), magna(), and cum_laude() generator functions. Each
#    honor is assigned based on a given GPA range listed below. Given a list
#    of input GPAs, create a generator function called honors_generator
#    that takes in 1 input argument named gpas that represents the list of 
#    GPAs from the variable gpas. The function should use yield from
#    on each input GPA to determine the honors assignment.
#
#    Honors Assignment               GPA
#    Summa Cum Laude                 > 3.9
#    Magna Cum Laude                 > 3.7
#    Cum Laude                       > 3.5
#
# 7. Call the connected generator function honors_generator with the gpas
#    list and set it to a variable called honors. Loop through the honors 
#    generator and print out each honor_label value to see which honors
#    labels will be generated given the gpas list.

def summa():
  yield 'Summa Cum Laude'

def magna():
  yield 'Magna Cum Laude'

def cum_laude():
  yield 'Cum Laude'

def graduation_countdown(days):
  while days > 0:
    days_left = yield days # could i write yield days for the same output?
    if days_left != None:
      days = days_left
    else:
      days -= 1

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()

days = 25
gpas = [3.2, 4.0, 3.6, 2.9]

countdown_generator = (day for day in range(days, -1, -1))

grad_days = graduation_countdown(days)

for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print(f'Days Left: {day}')

honors = honors_generator(gpas)

for honor_label in honors:
  print(honor_label)

