# Chap 9.2 - Dictionaries
# Using Dictionaries
# 2. Get A Key

# Get A Key
#
# Once you have a dictionary, you can access the values in it by providing the key.
# For example, let's imagine we have a dictionary that maps buildings to their 
# heights,  in meters: 
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#
# Then we can access the data in it like this:
print(building_heights["Burj Khalifa"])
print(building_heights["Ping An"])
#

# Tasks
# 1. We have provided a dictionary that maps the elements of astrology to the zodiac
#    signs. Print out the list of zidiac signs associated with the "earth" element.
#
# 2. Print out the list of the "fire" sign

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])
