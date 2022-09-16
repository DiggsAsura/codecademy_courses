# Chapter 11 - Classes
# 3. Project
# 1. Basta Fazoolin'

# You've started position as the lead programmer for the family-style Italian
# resturant Basta Fazoolin' with My Heart. The resturant has been doing fantastically
# and seen a lot of growth lately. You've been hired to keep things organized.

# Tasks
# Actually, this list is sooo long I don't care about writing it all down. 

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        welcome = "{} menu is available from {} to {}".format(self.name, self.start_time, self.end_time)
        return welcome
    
    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill
    
brunch = Menu("Brunch", {'panca kes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)
early_bird = Menu("Early-Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)
dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)
kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

#print(brunch)
#print(early_bird)
#print(dinner)
#print(kids)
#print(brunch.calculate_bill(['pancaces', 'home fries', 'coffee']))
#print(early_bird.calculate_bill(['salumeria plate', 'vegan mushroom ravioli']))

# First half. Had to get some help with the calculate_bill method, but I was on the right track, just had to get down the self.
# Need a small break to pick up GF. Will commit the first half.

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        welcome = "Welcome to Basta Fazoolin, {}".format(self.address)
        return welcome
    
    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu
 
    
menus = [brunch, early_bird, dinner, kids]
    
flagship_store = Franchise("1232 West End Road", menus)
new_installement = Franchise("12 East Mulberry Street", menus)

print(flagship_store)
print(new_installement)
    
print(flagship_store.available_menus(12))
print(new_installement.available_menus(17))


# Last third of the project. I am not sure if it's me thats slow or what - but here
# the tasks are kinda clear as mud, checked the video - and he kinda just go 
# through it in somewhat messy way. Oh well. 

# Arepa 
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
        
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installement])

arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("Take a' Arepa", arepas_items, 10, 20)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepa = Business("Take a' Arepa", [arepas_place])

print(arepa.franchises[0].menus[0])


# Well half of this was pretty easy, half was kinda messy. I guess I'm going to 
# work alot more with classes, so I hope I will learn it somehow. 