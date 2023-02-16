# Chap 9.1 - Dictionaries
# Creating Dictionaries
# 8. Dict Comprehensions

# Dict Comprehensions
#
# Let's say we have two lists that we want to combine into a dictionary, like a list
# of students and a list of their heights, in inches: 
#names = ['Jenny', 'Alexus', 'Sam', 'Grace']
#heights = [61, 70, 67, 64]
#
# Python allows you to create a dictionary using a dict comprehension, with this syntax:
#students = {key:value for key, value in zip(names, heights)}
#print(students)
# (oh my, this was a mouthfull)
# 
# Remember that zip() combines two lists into an iterator of tuples with the list
# elements paired together (YEA right, remember that lol. TRY try try). This dict
# comprehension: 
# 	1. Takes a pair from the iterator of tuples
#   2. Names the elements in the pair key (the one originally from the names
#			 list) and value (the one originally from the heights list)
#   3. Creates a key:value item in the students dictionary
#   4. Repeats steps 1-3 for the entire iterator of pairs

# Omg, ok this one will take some time. When we went through list comprehensions earlier
# I dont't feel it went deep enough, so it havent really stuck (kinda same with while
# loops really). I could barly remember zip() too. That means, i didn't remember. 
# Oh well. Let's push on. It's all about getting it into the blood, even if it's gonna
# take some time. 

# Tasks
# 1. You have two lists, representing some drinks sold at a coffee shop and the
#    milligrams of caffeine in each. First, create a variable zipped_drinks that is
#    an iterator of pairs between the drinks list and the caffeine list
#
# 2. Create a dictionary called drinks_to_caffeine by using a dict comprehension that
#    goes through the zipped_drinks iterator and turns each tuple pair into a 
#    key:value item

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Had to look at hints.. 
zipped_drinks = zip(drinks, caffeine)
#print(zipped_drinks) 
# to check how it looks. It makes a two dimensional lists right?
# nope, it makes an hash(?) prints:
# <zip object at 0x7f3bd3463f00>
# ..but that changes every time I run it. 

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

# Ok, maybe it's not that bad actually! I wish there was more tasks with this tho
# to really get it into the blood. 


