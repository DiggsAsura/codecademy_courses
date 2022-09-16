# Chapter 11 - Classes
# 1. Introduction to Classes
# 12. Everything is an Object

# Attributes can be added to user-defined objects after instantiation, so it's 
# possible for an object to have some attributes that are not explicitly defined
# in an object's constructor. We can use the dir() function to investigate an 
# object's attributes at runtime. dir() is short for directory and offers an 
# organized presentation of object attributes. 
#
#class FakeDict:
#  pass
# 
#fake_dict = FakeDict()
#fake_dict.attribute = "Cool"
# 
#print(dir(fake_dict))
#
# That's certainly a lot more attributes than we defined! Python automatically adds 
# a number of attributes to all objects that get created. These internal attributes
# are usually indicated by double-underscores. But sure enough, attribute is 
# in that list. 
#
# Do you remember being able to use type() on Python's native data types? This is 
# because they are also objects in Python. Their classes are int, float, str, 
# list and dict. These Python classes have special syntax for their instantiation, 
# 1, 1.0, "hello", [] and {} specifically. But these instances are still full-blown
# objects to Python.
#
#fun_list = [10, "string", {'abc': True}]
#for i in fun_list:
#	print(type(i))
#	print(dir(i))

#print(type(fun_list))
#print(dir(fun_list))
#
# Above we define a new list. We check it's type and see that's an instantiation of
# class list. We use dir() to explore its attributes, and it gives us a large number
# of internal Pythnon dunder attributes, but, afterward, we get the usual list
# methods. 

# Tasks
# 1. Call dir() on the number 5. Print the results
#
# 2. Define a function called this_function_is_an_object. It can take any parameters
# 	 and return anything you'd like
#
# 3. Print out the result of calling dir() on this_function_is_an_object

dir(5)

def this_function_is_an_object(hello):
	return "okay man"
	
print(dir(this_function_is_an_object))

