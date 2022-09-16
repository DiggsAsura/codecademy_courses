# Learn Intermediate Python 3
# 4. Object-Oriented Programming
# 2. Object-Oriented Programming
# 11. Getters, Setters and Deleters

print("\n --- Introduction --- ")
print(" -------------------- \n")

# Using getter, setter, and deleter functions are one way to implement encapsulation
# within Python where the state of class attributes can be handled within the class.
# These functions are useful in making sure that the data being handled is appropriate
# for the defined class functionality.

class Animal:
  def __init__(self, name):
    self._name = name
    self._age = None

  def get_age(self):
    return self._age
  
  def set_age(self, new_age):
    if isinstance(new_age, int):
      self._age = new_age
    else:
      raise TypeError
    
  def delete_age(self):
    print("_age Deleted")
    del self._age

# Looking at the Animal class above there is an _age attribute with a single underscore. This
# notates it is intended to be used only within the module. There are then 3 methods related to 
# age, each with a different purpose. These define the getter, setter and deleter of the 
# specific property.
#
# The first method related to age is a getter and returns self._age. The setter is implemented
# below that. It includes logic that ensures that the value passed to new_age is an integer.
# If so, self._age = new_age. If not, raise an error. This is useful and shows the power of using 
# these functions for encapsulation.
#
# The deleter is implemented below the setter. It outputs a confirmation message and uses 
# the del keyword to delete the self._age attribute.

a = Animal("Rufus")
print(a.get_age()) # None

a.set_age(10)
print(a.get_age()) # 10

#a.set_age("Ten") # Raises a TypeError

#a.delete_age() # "_age Deleted"
#print(a.get_age()) # Raises a AttributeError

# Above we see a.get_age() gets the _age value, a.set_age(10) sets the value and a.delete_age() 
# deletes the attribute entirely. A TypeError occurs with a.set_age("Ten") because the defined
# logic in the setter is looking only for an integer. An AttributeError occurs with 
# a.get_age() after the attribute was deleted.



print("\n --- Tasks --- ")
print(" ------------- \n")

# 1. Using a getter, setter, and the single underscore naming convention, the employees of
#    the company will now be able to use their names. The single underscore attribute _name
#    has been added to the Employee class. Names default to None unless a string argument
#    is passed during instantiation.
#
#    Inside the Employee class:
#
#     - Define a getter method called get_name() that returns the class attribute _name
#
# 2. Add a setter method.
#    
#    Inside the Employee class:
#
#     - Define a setter method set_name that has an additional parameter for the name string
#       and sets the class attribute _name
#
# 3. Lastly, Add a deleter method.
#
#    Inside the Employee class:
#
#     - Define a deleter method del_name that deletes the attribute.
#
# 4. Great job defining the getter and setter. Uncomment the code at the bottom of script.py
#    to test out the getter, setter and deleter.
#
#    Move on to the next exercise to wrap up the lesson!

class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name
  
  def get_name(self):
    return self._name
  
  def set_name(self, new_name):
    self._name = new_name
    return new_name

  def del_name(self):
    del self._name

e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
#print(e2.get_name())



# Having some issues with the setter.