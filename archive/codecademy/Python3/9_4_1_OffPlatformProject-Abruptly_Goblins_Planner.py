# Chap 9.4 - Dictionaries
# OffPlatform Project
# Abruptly Goblins Planner

# Introduction
# 
# Opening your comic book store, the Sorcery Society, has been a lifelong dream come
# true. You quickly diversified your shop offerings to include miniatures, plush toys, 
# collectible card games, and board games. Eventually, the store became more a games 
# store with a selection of this week's newest comic books and a small offering of 
# graphic novel paperbacks. Completing your transformation means offering space for 
# local tabletop gamers. They love to play their favorite RPG, "Abruptly Goblins!"
# and will happily pay you per chair to secure the space to do it. 
# Unfortunately, planning the game night has fallen to you. If you pick the wrong 
# night, not enough people will come and the game night will be cancelled. You 
# decide it's best that you automate the game night selector to get the most
# people through the door. First you need to create a list of people who will be
# attending the game night. 

# Instructions
# 1. Create an empty list called gamers. This will be your list of people who are
#    attending game night. 
# 
# 2. Now we want to create a function that will update this list and ad a new gamer
# 	 to the gamers list. Each gamer should be a dictionary with the following keys:
# 
# 	 - "name": a string that contains the gamer's full or presumed name. E.g. 
# 		 "Viky Very"
#		 - "availability": a list of strings containing the names of the days of the week 
# 		 that the gamer is available. E.g., "["Monday", "Thursday", "Sunday"]
#    
#    Create a function called add_gamer that takes two parameters: gamer and 
#		 gamers_list. The function should check that the argument passed to the gamer 
#    parameter has both "name" and a "availability" as keys and if so add gamer
#    to gamers_list
#
# 3. Next we want to add our first gamer! Her name is Kimberly Warner and she's 
#    available on Mondays, Tuesdays and Fridays. 
#
#    a) Create a dictionary called kimberly with the name and availability given above
#    b) Call add_gamer with kimberly as the first argument and gamers as the second.
#
# 	 Great! Let's add a couple more gamers to the list (prefilled from the Jupyter 
#    Notebook) 
#
# Finding the perfect availability
# 
# 4. Now that we have a list of all the people interested in game night, we want to 
#    able to calculate which nights would have the most participation. First we 
#    need to create a frequency table which correlates each day of the week with
#    gamer availability.
#
#    Create a function called build_daily_frequency_table that takes no arguments 
#    and returns a dictionary with the days of the week as keys and 0's for values.
#    We'll be using this to count the availabiltiy per night. Call 
#    build_daily_frequency_table and save the results to a variable called
#    count_availability.
#
# 5. Next we need to count the number of people every night. 
#
#    Write a function called calculate_availability that takes a list of gamers
#    as an argument gamers_list and a frequency table available_frequency. The 
#    function should iterate through each gamer in gamers_list and iterate through 
#    each day in the gamer's availability. For each day in gamer's availability,
#    add one to that date on the frequency table. 
#
# 6. Now let's use these tools to find the best night to run Abruptly Goblins!
#
#    Call calculate_availability with gamers and count_availability. Print out
#    count_availability afterward.
#
# 7. Lastly we need a way to pick the day with the most available people to attend
#    so that we can schedule game night on that night
# 
#    Write a function find_best_night that takes a dictionary availability_table
#    and returns the key with the highest number.
#
# 8. Now let's find the best day to host game night. 
#
#    Call find_best_night with count_availability, store the result in a variable
#    called game_night. Print out game_night to find out which day it is. 
#
# 9. And let's make a list of all the people who are available that night.
#
#    - Create a function available_on_night that takes two parameters: gamers_list
#      and day and returns a list of people who are available on that day.
#    - Call available_on_night with gamers and game_night and save the result 
#      into the variable attending_game_night.
#    - Print attending_game_night.
#
# Generating an E-mail for the Participants
# 
# With the best day for Abruptly Goblins! determined with computer precision, we 
# need to let the attendees know that the game night is on a night they can attend.
# Let's start by creating a form email to send to each of the participants that 
# we'll fill out with data later. 
#
# 10. Define a string, called form_email with interpolation variables {name}, 
#     {day_of_week} and {game} (in case we decide we want to use this featureset 
#     to host a different game night). 
#     Use it to tell your gaming attendees the night their Abrptly Goblins! 
#     can be played.
#
# 11. Create a function send_email with three parameters: gamers_who_can_attend, 
#     day and game. Print form_email for each gamer in gamers_who_can_attend with 
#     the appropriate day and game. Call send_email with attending_game_night, 
#     game_night, and "Abruptly Goblins!". 
#
# Afterward
#
# You feel bad for the folks who weren't able to attend on the decided upon game 
# night, and try to use your currently written methods to have a second night of 
# the week. 
#
# 12. - Create a list unable_to_attend_best_night of everyone in gamers that 
#       wasn't able to attend game night on game_night
#     - Create second_night_availability frequency table by calling 
#       build_daily_frequency_table
#     - Call calculate_availability with unable_to_attend_best_night and 
#       second_night_availability
#     - Call find_best_night with the now filled-in second_night_availability, 
#       save the results in second_night.
#
# 13. Let's send out an email to everyone (whether they can attend the first night 
#     or not) whose marked themselves as available on our second game night. 
#
#     - Create the list available_second_game_night by calling available_on_night
#       with gamers and second_night
#     - let the gamers know by calling send_email with available_second_game_night, 
#       second_night and "Abruptly Goblins!"


gamers = []

def add_gamer(gamer, gamers_list):
	if gamer.get("name") and gamer.get("availability"):
		gamers_list.append(gamer)
	else:
		print("Gamer missing critical information")

kimberly = {
	'name': "Kimberly Warner", 
	'availability': ["Monday", "Tuesday", "Friday"]
}
add_gamer(kimberly, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
	
#print(gamers)

def build_daily_frequency_table():
	return {
		"Monday": 0,
		"Tuesday": 0,
		"Wednesday": 0,
		"Thursday": 0,
		"Friday": 0,
		"Saturday": 0,
		"Sunday": 0,
	}

count_availability = build_daily_frequency_table()

#print(count_availability)

def calculate_availability(gamers_list, available_frequency):
	for gamer in gamers_list:
		for day in gamer['availability']:
			available_frequency[day] += 1

calculate_availability(gamers, count_availability)
#print(count_availability)

def find_best_night(availability_table):
	best_availability = 0
	for day, availability in availability_table.items():
		if availability > best_availability:
			best_night = day
			best_availability = availability
	return best_night

game_night = find_best_night(count_availability)
#print(game_night)

def available_on_night(gamers_list, day):
	return [gamer for gamer in gamers_list if day in gamer['availability']]

attending_game_night = available_on_night(gamers, game_night)
#print(attending_game_night)


# E-mail

form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. 
Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""

def send_email(gamers_who_can_attend, day, game):
	for gamer in gamers_who_can_attend:
		print(form_email.format(name=gamer['name'], day_of_week=day, game=game))
		
#print(send_email(attending_game_night, game_night, "Abruptly Goblins!"))


unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

#print(second_night)

available_second_game_night = available_on_night(gamers, second_night)
print(send_email(available_second_game_night, second_night, "Abruptly Goblins!"))


# These fuckgin Jupyter Notebook tasks is a nightmare. First off, they are overly complicated for our level 
# at this stage (for me at least), and it's just a fucking mess, the whole notebook thingy. IDK why people like it
# I just hate it haaard and every time one of these off platform projects show up I allmost loose motivation
# to do anything. Fucckking fuck
# Fuck jupyter notebook. 
# amen.


