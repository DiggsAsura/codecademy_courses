inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Task 1 - how many items in the list
inventory_len = len(inventory)
print(inventory_len)

# Task 2 - print the first item in the list. Remember []
first = inventory[0]
print(first)

# Task 3 - last item in inventory
last = inventory[-1]
print(last)

# Task 4 - slice from 2 to 6 (not include the 6th item)
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

# Task 5 - first 3
first_3 = inventory[:3]
print(first_3)

# Task 6 - count twin beds)
twin_beds = inventory.count("twin bed")
print(twin_beds)

# Task 7 - remove the 5th element with pop
removed_item = inventory.pop(4)
print(removed_item)

# Task 8 - Add item "19th Century Bed Frame" in slot 11
# failed couple of times, remember int first!
inventory.insert(10, "19th Century Bed Frame")
print(inventory)

# Task 9 - sort list .sort() .sorted()
sorted_inventory = sorted(inventory)
print(inventory)
inventory.sort()
print(inventory)