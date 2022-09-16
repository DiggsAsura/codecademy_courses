# Chapter 6 - Python Code Challenges
# Functions 3
# Win Percentage

# Next, we will create a function which calculates the percentage of games won. In order to do this, we need
# to kno how many total games there were and divide the number of wins by the total number of games. For this
# function, there will be two input parameters, the number of wins and the number of losses. We also need to 
# make sure that we return the result as a percentage (in the range of 0 to 100). In order to create
# this method we need the following steps:

# 1. Define the function header with two parameters, wins and losses
# 2. Calculate the total number of games using the number of wins and losses
# 3. Get the ratio of winning using the number of wins out of the total number of games. 
# 4. Convert the ratio to percentage
# 4. Return the percentage

# Ok had this one before. I think I remember it, but maybe not the part of returning as percentage. Let's see how 
# goes. 

def win_percentage(wins, losses):
	#total_matches = wins + losses
	#ratio = wins / total_matches
	#return ratio
	
	# I kenw i wrote this in one line before. Just tested the longer clunkier code - but it does not work. How come? 
	#return wins / range(wins + losses)
	# Ok noob listen, read your challenge. This apparently was a slightly modified version, where they wanted the
	# percentage, which I could not remember from before. Ofc, add it up with 100.. This makes the first long
	# code perfectly fine too, if i just had multiplied with 100. Moron :D 
	return wins / (wins + losses) * 100
	
	
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
