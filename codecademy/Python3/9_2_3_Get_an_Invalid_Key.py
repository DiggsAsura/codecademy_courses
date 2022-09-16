# Chap 9.2 - Dictionaries
# Using Dictionaries
# 3. Get an Invalid Key

# Get an Invalid Key
#
# Let's say we have our dictionary of building heights from the last exercise:
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#
# What if we wanted to know the height of the Landmark 81 in Ho Chi Minh City? We
# could try:
#print(building_heights["Landmark 81"])
#
# But "Landmark 81" does not exist as a key in the building_heights dictionary! So 
# this will throw a KeyError:
# KeyError: 'Landmark 81'
#
# One way to avoid this error is to first check if the key exist in the dictionary:
key_to_check = "Landmark 81"
if key_to_check in building_heights:
	print(building_heights["Landmark 81"])
else: 
	print("Not in the dictionary")
#
# This will not throw an error, because key_to_check in building_heights will return
# False, and so we never try to access the key.

# Tasks
# 1. Run the code. It should throw a KeyError! "energy" does not exist as one of 
#		 the elements.
#
# 2. Add the key "energy" to the zodiac_elements. It should map to a value of 
#		 "Not a Zodiac Element". Run the code. Did this resolve the KeyError?

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"])

