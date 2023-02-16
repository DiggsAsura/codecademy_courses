# Chap 9.1 - Dictionaries
# Creating Dictionaries
# 5. Add A Key

# Add A Key
# To add a single key: value pair to a dictionary, we can use the syntax:
# dictionary[key] = value
#
# For example, if we had our menu dictionary from the first exercise:
#menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# 
# And we wanted to add a new item, "cheesecake" for 8 dollars, we could use: 
#menu["cheesecake"] = 8
#print(menu)
#
# Now, menu looks like: 
# {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}

# Tasks
# 1. Create an empty dictionary called animals_in_zoo. 
# 2. Walking around the zoo, and you see 8 zebras. Add "zebras" to animals_in_zoo as a
#    key and with a value of 8.
# 3. The primate house was bananas! Add "monkeys" to animals_in_zoo as a key with 
#    value of 12. 
# 4. As you leave the zoo, you are saddened that you did not see any dinosaurs. Add
#    "dinosaurs" to animals_in_zoo as a key with a value of 0. 
# 5. Print animals_in_zoo

animals_in_zoo = {}

animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0

print(animals_in_zoo)
