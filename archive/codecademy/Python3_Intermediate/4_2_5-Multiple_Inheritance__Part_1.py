# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 5. Multiple Inheritance: Part 1

print("\n --- Introduction --- ")
print(" -------------------- \n")
# Let's now look at a feature allowed by Python called multiple inheritance.
# As you may have guessed from the name, this is when a subclass inhertis
# from more than ne superclass. One form of multiple inheritance is when
# there are multiple levels of inheritance. This means a class inherits 
# members from its superclass and its super-superclass.
class Animal:
  def __init__(self, name):
    self.name = name
    
  def say_hi(self):
    print("{} says, Hi!".format(self.name))
    
class Cat(Animal):
  pass

class Angry_Cat(Cat):
  pass

my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi()

# In the above example, Angry_Cat inherits from Cat and Cat inherits from 
# Animal. Both Angry_Cat and Cat have access to the Animal class name attribute
# and .say_hi() method. Any feature added to Cat, Angry_Cat will also
# have access to. 

print("\n --- Tasks ---")
print(" ------------- \n")

# Tasks
# 1. Managers decide to start walking around more to let people know who
#    is in charge. 
#
#    Inside script.py:
#     - Define a Manager class and have it inherit from the Admin class
#     - Inside the Manager class, define a method say_id() that outputs
#       they are in charge. 
#
# 2. The Managers want to set a good example so they also let people know
#    their ID and that they are an admin. 
#
#    Inside the .say_id() method of Managers:
#     - Call the Admin class .say_id() method
#
# 3. Now test it out. 
#
#    Athe the bottom of script.py:
#     - Define a variable e4 and set it to be an instance of the Manager
#       class
#     - Call the .say_id() method of the instance in e4
#
#    Now you will get output from all 3 classes. 

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
    print("I am an admin.")
    
class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am a manager.")
    

e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()

#e3.say_id()
e4.say_id()



# This is cool stuff!