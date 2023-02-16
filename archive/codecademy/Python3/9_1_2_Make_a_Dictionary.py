# Chap 9.1 - Dictionaries
# Creating Dictionaries
# 2. Make a Dictionary

# Make a Dictionary
#
# In the previous exercise, we saw a dictionary that maps strings to numbers
# (i.e., "avocado toast": 6). However, the keys can be numbers as well. 
#
# For example, if we were mapping resturant bill subtotals to the bill total after 
# tip, a dictionary could look like: 
#
#subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
#
# Values can be of any type. We can use a string, a number, a list, or even another
# dictionary as the value associated with a key!
#
# For example:
#students_in_classes = {"software design": ["Aron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
#
# The list ["Aron", "Delila", "Samson"], which is the key value for the key 
# "software_design", represents the students in that class. 
#
# We can also mix and math key and value types. For example:
#person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

# Tasks
# 1. Create a dictionary called translations that maps the following words in 
#    English to their definitions in Sindarin (the language of the elves):
#    English			Sindarin
#		 mountain			orod
#    bread				bass
#    friend				mellon
#		 horse				roch

translations = {"mountain": "orod", "bread": "orod", "friend": "mellon", "horse": "roch"}

print(translations)
