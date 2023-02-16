# Chap 9.1 - Dictionaries
# Creating Dictionaries
# 6. Add Multiple Keys

# Add Multiple Keys
# If we wanted to add multiple key: value pairs to a dictionary at once, we can use the 
# .update() method.
#
# Looking at our sensors object from a previous exercise: 
#sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
#
# If we wanted to add 3 new rooms, we could use: 
#sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
#print(sensors)
#
# This would add all three rooms to the sensors dictionary. 
#
# Now, sensors looks like: 
# {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}

# Tasks
# 1. In one line of code, add two new users to the user_ids dictionary
# 		- theLooper, with an id of 138475
#			- stringQueen, with an id of 85739
# 2. Print user_ids

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# Really motivated today for coding. Just wanna code all day. Family life makes it 
# tricky, but yea I just enjoy that feeling! Super happy about have signed up for 
# the Codecademy pro plan (no plug lol)

