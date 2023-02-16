# Chap 9.1 - Dictionaries
# Creating Dictionaries
# 7. Overwrite Values

# Overwrite Values
# 
# We know that we can add a key by using syntax like
# menu["avocado toast"] = 7
#
# This will create a key "avocado toast" and set the value to 7. But what if we 
# already have an 'avocado toast' entry in the menu dictionary?
#
# In that case, our value assignment would overwrite the existing value attached to the
# key 'avocado toast'. 
#
#menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#menu["oatmeal"] = 5
#print(menu)
#
# This would yield
# {"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
#
# Notice the value of "oatmeal" has now changed to 5. 

# Tasks
# 1. Add the key "Supporting Actress" and set the value to "Viola Davis". 
# 2. Without changing the definition of the dictionary oscar_winners, change the 
#    value associated with the key "Best Picture" to "Moonlight".

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", " Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

# Checking if I can remove entry. Some back and forth in the community forums. 
oscar_winners.pop("Best Picture")
# Indeed, could do with .pop() :) 
print(oscar_winners)
