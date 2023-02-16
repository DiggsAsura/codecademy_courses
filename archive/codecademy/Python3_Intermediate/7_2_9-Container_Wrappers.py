# 7. Specialized Collections
# 2. Collections
# 9. Container Wrappers

from re import A


print('\nContainer Wrappers\n-----------------')

# In Python, wrappers are modifications to functions or classes which change the
# behavior in some way. They are called wrappers because they "wrap" around
# the existing code to modify it. This is most commonly used with function
# wrapping, but we can also wrap classes. Let's take a look at an example
# of a class wrapper.
#
# First, we need a class to wrap acount:

class Customer:
  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number

# Next, we create a wrapper class which stores an object of the class we are
# wrapping around. It also includes some additional functionality.

class CustomerWarp(Customer):
  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)

  def display_customer_info(self):
    print(f'Name: {self.customer.name}')
    print(f'Age: {self.customer.age}')
    print(f'Address: {self.customer.address}')
    print(f'Phone Number: {self.customer.phone_number}')

# Finally, we can create an object from the wrapper class to access the new 
# functionality and the wrapped class contained inside. 

customer = CustomerWarp('Dimitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()

# Wrapper classes allow us to create different variations of classes with
# different purposes while avoiding duplicate code. Since we use an instance
# of the wrapped class inside of it, it preserves all of the attributes
# and methods from the wrapped class and keeps us from having to re-type all
# of the code.
#
# In the case of containers, the collections class has three different wrapper 
# classes set up for us to modify! Because of this, we can refer to them as
# wrapper containers. The advanced containers which we have already been looking
# at are variations of the standard built-in containers, so using wrapper
# containers allows us to create our own versions as well.
#
# The three wrapper containers we will be looking at are:
#
#     - UserDict
#
#     - UserList
#
#     - UserString
#

print('\n"Tasks"\n-----------')
# No tasks:
# Take a look at the provided CustomerWrap class. Play around with the code 
# and then click Next to move on!

class Customer2: 
  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number

class Customer2Wrap(Customer2):
  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)
  
  def display_customer_info(self):
    print(f'Name: {self.customer.name}')
    print(f'Age: {self.customer.age}')
    print(f'Address: {self.customer.address}')
    print(f'Phone Number: {self.customer.phone_number}')

customer2 = Customer2Wrap('Kenneth B. Bjerke', 37, 'Some street, Kongsberg', '96621811')
customer2.display_customer_info()