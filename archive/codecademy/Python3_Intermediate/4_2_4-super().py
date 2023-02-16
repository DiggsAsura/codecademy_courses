# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 4. super()

# When overriding methods we sometimes want to still access the behavior 
# of the parent method. In order to do that we need a way to call the method 
# of the parent class. Python gives us a way to do that using super().
#
# super() gives us a proxy object. With this proxy object, we can invoke the
# method of an object's parent class (also called its superclass). We call
# the required function as a method on super():

print(" --- Example ---\n")
# ============================

class Animal:
  def __init__(self, name, sound="Grrrr"):
    self.name = name
    self.sound = sound
    
  def make_noise(self):
    print("{} says, {}".format(self.name, self.sound))
    
class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow!")

pet_cat = Cat("Rachel")
pet_cat.make_noise()

# Output:
# Rachel says, Meow!

# In the above example, we have the class Animal and the subclass Cat. Animal
# has 2 attributes, name and sound and one method, .make_noise(). The
# .make_noise() method outputs the name and sound of an instance. 
#
# The Cat subclass has an .__init__() method which means the .__init__()
# method of its superclass, Animal will not be called when creating an 
# instance of Cat. The .__init__() method from the subclass is overriding the 
# one from the superclass.
#
# To still invoke the .__init__() method of Animal, super().__init__(name, 
# "Meow!") is called inside the subclass .__init__() method. This additional 
# logic allows us to add the "Meow" sound from within the Cat class, but
# still use the .__init__() method of the Animal class.
#
# super() is used in subclasses to invoke a needed behavior from the 
# superclass alongside the behavior of a subclass method.


# ===
print('\n\n --- Tasks ---\n')
# ==============================

# 1. Once the managers found out that the admins were walking around just
#    telling people they are admins, the managers stepped in and made them
#    also say their ID. 
#
#    Inside the Admin class:
#     - Add a line that also calls the Employee class .say_id() method
#
#    Now the output should be the admin's ID and that they are an admin.

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
    
  def say_id(self):
    print("My id is {}".format(self.id))
    
class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

# A bit "new" to me to do ().(), even though I have done it via variables many
# times. Makes sense tho!

