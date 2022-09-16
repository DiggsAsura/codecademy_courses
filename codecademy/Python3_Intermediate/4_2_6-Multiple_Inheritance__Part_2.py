# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 6. Multiple Inheritance: Part 2

print("\n --- Introduction --- ")
print(" -------------------- \n")
# Another form of multiple inheritance involces a subclass that inherits
# directly from two classes and can use the attributes and methods of both.

class Animal:
  def __init__(self, name):
    self.name = name
    
class Dog(Animal):
  def action(self):
    print("{} wags tail. Awwww".format(self.name))

class Wolf(Animal):
  def action(self):
    print("{} bites. OUCH!".format(self.name))

class Hybrid(Dog, Wolf):
  def action(self):
    super().action()
    Wolf.action(self)

my_pet = Hybrid("Fluffy")
my_pet.action()

# Output:
# Fluffy wags tail. Awwww
# Fluffy bites. OUCH!

# The above example shows the class Hybrid is a subclass of both Dog and 
# Wolf which are also both subclasses of Animal. All 3 subclasses can use
# the features in Animal and Hybrid can use the features of Dog and Wolf.
# But, Dog and Wolf can not use each other's features.
#
# This form of multiple inheritance can be useful by adding functionality
# from a class that does not fit in with the current design scheme of the
# current classes.
#
# Care mus be taken when creating an inheritance structure like this, 
# especially when using the super() method. In the above example, calling
# super().action() inside the Hybrid class invokes the .action() method of
# the Dog class. This is due to it being listed before Wolf in the 
# Hybrid(Dog, Wolf) definition.
#
# The line Wolf.action(self) calls the Wolf class .action() method. The 
# important thing to note here is that self is passed as an argument. This
# ensures that the .action() method in Wolf receives the Hybrid class
# instance to ouput the correct name.
#

print("\n --- Tasks --- ")
print(" ------------- \n")

# 1. Admins in the company need access to the consumer-facing website. This 
#    means that admins must also be users of the site.
#
#    The class User has been added and has the attributes username and role
#    and the .say_user_info() method.
#
#    To get the admins the user access they need:
#     - Have the Admin class inherit from the User class alongside
#       the Employee class. Be sure to have the Employee class listed first
#       in the Admin class definition.
#
# 2. Now let's make sure the admins get their user data set up.
#
#    Inside the .__init__() method of the Admin class:
#     - Call the .__init__() method of the User class
#     - Pass the Admin class instance, id and the string "Admin" as
#       arguments to the .__init__() method call
#
# 3. Confirm the user data is set up correctly.
#     - Call the .say_user_info() method using the Admin instance in e3

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
  
  def say_id(self):
    print("My id is {}.".format(self.id))
  
class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))
      
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, "Admin")
  
  def say_id(self):
    super().say_id()
    print("I am an admin.")
    
e1 = Employee()
e2 = Employee()
e3 = Admin()

e3.say_user_info()

# Ok what arguments to pass was a bit conveluted. 