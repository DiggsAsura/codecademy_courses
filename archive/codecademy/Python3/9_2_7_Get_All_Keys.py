# Chap 9.2 - Dictionaries
# Using Dictionaries
# 7. Delete a Key

# Get All Keys
#
# Sometimes we want to operate on all of the keys in a dictionary. For example, if we
# have a dictionary of students in a math class their grades: 
#test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#
# We want to get a roster of the students in the class, without including their 
# grades. We can do this with the built-in list() function:
#print(list(test_scores))
#
# Dictionaries also have a .keys() method that returns a dict_keys object. A 
# dict_keys object is a "view" object, which provides a look at the current state
# of the dictionary, without the user being able to modify anything. The dict_keys
# object returned by .keys() is a set of keys in the dictionary. You cannot add or
# remove elements from a dict_keys object, but it can be used in the place of a 
# list for iteration:
#for student in test_scores.keys():
#	print(student)
# will yyield:
# Grace
# Jeffrey
# Sylvia
# Pedro
# Martin
# Dina
#
#print(test_scores.keys())
# yields
# dict_keys(['Grace', 'Jeffrey', 'Sylvia', 'Pedro', 'Martin', 'Diana'])

# Tasks
# 1. Create a variable called users and assign it to be a dict_keys object of all the 
#    keys of the user_ids dictionary.
#
# 2. Create a variable called lessons and assign it to be a dict_keys object of all 
#    the keys of the num_exercises dictionary.
#
# 3. Print users to the console.
#
# 4. Print lessons to the console

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

lessons = num_exercises.keys()

print(users)
print(lessons)


