# Lists Challenge (Advanced)
# Challenge 18
# More Frequent Item

# Let's go back to our factory example. We have a conveyor belt of items where each item is represented
# by a different number. We want to know, out of two items, which one shows up more on our belt. To solve 
# this, we can use a function with three parameters. One parameter for the list of items, another for the 
# first item we are comparing, and another for the second item. Here are the steps:

# 1. Define the function to accept three parameters: the list, the first item and the second item
# 2. Count the number of times item1 shows up in our list
# 3. Count the number of times item2 shows up in our list
# 4. If item1 shows up more, return item1. Otherwise, return item2

# Ok this one I think is easier. Now i remember theres a built-in function or method (whats the 
# difference really???) for count at least!

# OK so this was what I came up with, but it turns out i just got it the wrong order. 
# It's not item1.count(lst) of course, its lst.count(item1)

def more_frequent_item(lst, item1, item2):
	#if item1.count(lst) > item2.count(lst):
	# Next one would have been correct, if i read the full task... LEARN THIS! Lol. It should return item1 if they
	# got the same amount. Aka >=, not just >
	#if lst.count(item1) > lst.count(item2):
	if lst.count(item1) >= lst.count(item2):
		return item1
	else: 
		return item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
