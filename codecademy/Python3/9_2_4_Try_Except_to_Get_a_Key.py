# Chap 9.2 - Dictionaries
# Using Dictionaries
# 4. Try/Except to Get a Key

# Try/Except to Get a Key
#
# We saw that we can avoid KeyErrors by checking if a key is in a dictionary first.
# Another method we could use is a try/except:
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#
key_to_check = "Landmark 81"
try:
	print(building_heights[key_to_check])
except KeyError:
	print("That key doesn't exist!")  # cool stuff, this was new. 
#
# When we try to access a key that doesn't exist, the program will go into the 
# except block and print "That key doesn't exist!

# This one is useful I guess! Can it only be used with dictionaries? 

# Tasks
# 1. Use a try brock to try to print the caffeine level of "matcha". If there is a 
# 	 KeyError, print "Unknown Caffeine Level". 
#
# 2. Above the try block, add "matcha" to the dictionary with a value of 30

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level.update({"macha": 30})

try:
	print(caffeine_level["macha"])
except KeyError:
	print("Unknown Caffeine Level.")
	
# Ok so far this Dictionaries couse have been quite smooth! Knock on woods. 
