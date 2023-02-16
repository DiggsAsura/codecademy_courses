# Control Flow (Advanced)
# Challenge 9
# Movie Review

# We want to create a function that will help us rate movies. Our function will split the ratings into 
# different ranges and tell the user how the movie was based on the movies's rating. Here are the steps needed:

# 1. Define our function to accept a single number called rating
# 2. If the rating is equal to or less then 5, return "Avoid at all costs!"
# 3. If the rating was less than 9, return "This one was fun."
# 4. If neigher of the if statement conditions were met, returnn "Outstanding!"

# Ok first hunch here is basically if elif and else. Pretty straight forward right?
# at elif, gotta think. cant just do >= 9 - as it will double print, no? Use range()?
# Also, not clear if it want "python 9" or regular 9 meaning i have to 10. Lets see..
# Actually - it will read code from top to bottom right? So if the first if statement is True, it will print, if 
# not, it will check next, then else if neither? I guess >= 9 should do without range then! Gonna try both. 

#def movie_review(rating):
#	if rating <= 5:
#		print("Avoid at all costs!")
#	elif rating >= range(6,10):
#		print("This one was fun.")
#	else:
#		print("Outstanding!")

# Ok this is wrong, got the order wrong, looks like it's partially because of 5 = 6 etc in programming, but still
# not right. 

# Reading the task again.... Yea indeed mention range. Gotta rethink! use range()! 

#def movie_review(rating):
#	if rating <= range(5):
#		print("Avoid at all costs!")
#	elif rating == range(5, 9):
#		print("This one was fun.")
#	elif rating >= 9
#		print("Outstanding!")
		
# Also wrong. First one i have to lookup hint. I feel I'm kind of close, but no cigar. 
# Ooook so the range() was a step in the wrong direction. This is how they would write it. Idk, thought I 
# did try this but I guess not! Maybe typos idk... Anyhow! This is the solution.

# Note! Note i can just put the string into return without print()! They also just used two if without else.
# But also let me know can use both variants. 

def movie_review(rating):
	if(rating <= 5):
		return "Avoid at all costs!"
	elif(rating < 9):
		return "This one was fun."
	return "Outstanding!"
	
	
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."	
	
