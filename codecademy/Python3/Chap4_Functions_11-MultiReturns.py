# return can store more then one value, just remember to comma separate!

def top_tourist_locations_italy():
	first = "Rome"
	second = "Venice"
	third = "Florence"
	return first, second, third

# Failed - multireturns has to be written different
#most_popular1 = top_tourist_locations_italy(first)
#most_popular2 = top_tourist_locations_italy(second)
#most_popular3 = top_tourist_locations_italy(third)

# should be like this
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

# The lesson failed, but could still print the values like this
#print(most_popular1, most_popular2, most_popular3)

# Lesson ask for multiple print()'s
print(most_popular1)
print(most_popular2)
print(most_popular3)
