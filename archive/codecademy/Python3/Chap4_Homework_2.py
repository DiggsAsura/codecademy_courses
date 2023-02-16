# Make a function that calculate win percentage 

def win_percentage(wins, losses):
	return wins / (wins + losses) * 100
	
print(win_percentage(5, 5))
print(win_percentage(10,100000))


