# Chap 9.2 - Dictionaries
# Using Dictionaries
# 6. Delete a Key

# Delete a Key
#
# Sometimes we want to get a key and remove it from the dictionary. Imagine we were
# running a raffle, and we have this dictionary mapping ticket numbers to prizes: 
#raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
#
# When we get a ticket number, we want to return the prize and also remove that pair
# from the dictionary, since the price has been given away. We can use .pop() to do
# this. Just like with .get(), we can provide a default value to retrn if the key does
# not exist in the dictionary: 
#print(raffle.pop(320291, "No Prize"))
#print(raffle.pop(100000, "No Prize"))
#print(raffle.pop(872921, "No Prize"))
#print(raffle.pop(320291, "No Prize"))
#
# .pop() works to delete items from a dictionary, when you know the key value. 
#
# Ok this is freaking cool. Really feel I get more experience, and ideas how to use 
# this stuff! I just allmost can't wait for the classes lessons, as I feel that is
# the last major chapter i need to get down. 

# Tasks
# 1. You are designing the video game Big Rock Adventure. We have provided a 
#    dictionary of items that are in the players's inventory which add points 
#    to theirs health meter. In one line, add the corresponding value of the 
#    key "stamina grains" to health_points variable and remove the item 
#    "stamina grains" from the dictionary.
#    If the key does not exist, add 0 to health_points.
#
# 2. In one line, add the value of "power stew" to health_points and remove the
#    item from the dictionary. If the key does not exist, add 0 to health_points.
#
# 3. In one line, add the value of "mystic bread" to health_points and remove the 
# 	 item from the dictionary. If the key does not exist, add 0 to health points. 
#
# 4. Print available_items and health_points

# HAHAH, this is can pretty much directly be implemented into my project of making 
# the rpg. Great stuff. I had a big hunch dictionaries will be a major thing for 
# that. 

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strengh sandwitch": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points = health_points + available_items.pop("stamina grains", 0)
print(health_points)
health_points = health_points + available_items.pop("power stew", 0)
print(health_points)
health_points = health_points + available_items.pop("mystic bread", 0)
print(health_points)
