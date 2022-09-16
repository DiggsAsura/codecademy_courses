# Chap 7.2 - Strings
# String Methods
# 12. .format() II

# Goes a bit deeper to show how to use keywords. In the previous example, we just put empty {} inside the string
# which then relies on correct order of the arguments. This can be specified. In the example, they have to specify 
# a bit more though, not sure however if this is really needed? Tested. YES, it's needed to do the format
# like song=song, artist=artist. Order of arguments does not really matter now tho.

def favorite_song_statement(song, artist):
	return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)
	
print(favorite_song_statement("Crash and Die", "Mock Orange"))

# Task:
# 1. The function poem_description is supposed to use .format() to print out some quick information about a 
#    poem, but it seems to be causing some errors currently. 
#
#    Fix the function by using keywords in the .format() method
#
# 2. Run poem_description with the following arguments and save the results to the variable my_beard_description:
#    author = "Shel Silverstein"
#    title = " My Beard"
#    original_work = "Where the Sidewalk Ends"
#    publishing_date = "1974"

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc 
  
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)
print(my_beard_description)

# SO GDI... I had to change the order of arguments anyhow?!?!?!? Why? Makes no sense to me. We literally learn
# order does not matter but it does, with no explanation?? Ugg.. Positional arguments? In the forums I don't see
# any question or solution around this. I do see people start complaining more and more about codecademy though. 
