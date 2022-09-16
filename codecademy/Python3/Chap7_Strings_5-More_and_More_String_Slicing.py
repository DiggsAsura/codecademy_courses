# Chap 7 - Strings
# 5. More and More String Slicing (How Long is that String?)

# Touching on len() again, as one of the built-in functions to deal with strings. This one will count the 
# length. We done it a gazzilion times already, but I still like we are going over some of this again acatually. 
# Makes me feel less dumb xD

first_name = "Reiko"
last_name = "Matsuki"

# 1. Write a function called password_generator() that takes two inputs, first_name and last_name, and then 
#    concatenate the last three letters of each and returns them as a string
# 2. Test your function on the provided first_name and last_name and save it to the variable temp_password

# Okies, normally I would not deal with len() inside slicing here, but I guess this is what the lesson
# want me to do. 

def password_generator(first_name, last_name):
	return first_name[-3:] + last_name[-3:]
	
temp_password = password_generator(first_name, last_name)
print(temp_password)
