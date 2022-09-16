# Learn Intermediate Python 3
# 3. Functions Deep Dive
# 4. Decorators
# Video (Decorators)

# This is a 22 min video
# https://www.youtube.com/watch?time_continue=12&v=WOHsHaaJ8VQ&feature=emb_title

# 1. Functions are objects
def add_five(num):
  print(num + 5)
add_five(2)


# 2. Functions within functions
def add_six(num):
  def add_two(num):
    return num + 2
  
  num_plus_two = add_two(num)
  print(num_plus_two + 3)
add_six(10)


# 3. Returning functions from functions
def get_math_function(operation): # + or -
  def add(n1, n2):
    return n1 + n2
  def sub(n1, n2):
    return n1 - n2
  
  if operation == '+':
    return add
  elif operation == '-':
    return sub

add_function = get_math_function('+')
sub_function = get_math_function('-')

print(add_function(4, 6))
print(sub_function(4, 6))


# 4. Decorating a function / 5 combined
def title_decorator(print_name_function):
  def wrapper():
    print("Dr:")
    print_name_function()
  return wrapper

@title_decorator
def print_my_name():
  print("Kenneth")
@title_decorator
def print_joes_name():
  print("Joe")

print_joes_name()

#decorated_function = title_decorator(print_my_name)
#decorated_function()

#decorated_function2 = title_decorator(print_joes_name)
#decorated_function2()
#print(decorated_function)

# Holy, this might be very useful. do a @function to pass in the following
# function.

# 5. Decorators
# See above

# 6. Decorators w/ Parameters

def title_decor(print_name_function):
  def wrapper(*args, **kwargs):
    print("Professor:")
    print_name_function(*args, **kwargs)
  return wrapper

@title_decor
def print_name(name, age):
  print(name + " you are " + str(age)) 

print_name("Kenneth", 37)

# NICE! This can be very useful. Just have to let it grow a bit, I have 
# a hunch this can be quite useful. 