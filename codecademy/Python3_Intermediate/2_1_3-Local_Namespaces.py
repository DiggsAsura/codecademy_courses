# Learn Intermediate Python 3
# 2. Namespaces and Scope
# 1. Namespaces
# 3. Local Namespace

#global_variable = 'global'

#def add(num1, num2):
#  nested_value = "Inside Function"
#  print(num1 + num2)
#  print(locals())

#add(5, 10)

#local_stuff = locals()
#global_stuff = globals()

#if local_stuff == global_stuff:
#  print("Identical")
#else: 
#  print("Not identical")

# Note:
# - We called locals() inside the add() function to get the local namespace
#   generated when the function is executed. If we called locals() outside 
#   of a function in our program, it behaves the same as globals().
#
# - The value printed from calling locals() represents the namespace that
#   only exists inside of the function. Notice even the function parameters
#   num1 and num2 exist alongside the variable name nested_value. The 
#   namespace does not include global_variable since it exists outside of
#   the function (in the global namespace)

# Ok so the local namespace is inside functions only? 

global_variable = 'global'


print(' -- Local and global Namespaces with empty script -- \n')
print(locals())
print(globals())

def divide(num1, num2):
  result = num1 / num2
  print(locals())

def multiply(num1, num2):
  product = num1 * num2
  print(locals())

print(' \n -- Local Namespace for divide -- \n')
divide(3, 4)

print(' \n -- Local Namespace for multiply -- \n')
multiply(4, 50)

print(' \n -- Local Namespace final -- \n')
print(locals())


# Ok yea, so local namespaces shows the same as global namespaces if it's 
# called outside a function (guess maybe a class too?)
# Is this solely theoretical stuff or actually important to know in practice?
