# Chap 9.2 - Dictionaries
# Using Dictionaries
# 10. Review

# Review
#
# In this lesson, you've learned how to go through dictionaries and access keys 
# and values in different ways. Specifically, you have seen how to: 
#
# 	- Use a key to get a value from a dictionary
#		- Check for existence of keys (try/except)
#		- Remove a key: value pair from a dictionary (pop) 
#		- Iterate through keys and values in dictionaries
#

# Never been this motivated I think. I have to admit, I do not think Python going
# to be my main language. I use it to learn programming, and will focus on it for 
# a couple more monhts. But I grow more and more sure that Rust will be where I 
# go all in. 

# Tasks
# 1. We have provided a pack of tarot cards, tarot. You are going to do a three
# 	 card spread of your past, present and future. 
#
# 	 Create an empty dictionary called spread.
#
# 2. The first card you draw is card 13. Pop the value assigned to the key 13 out 
#    of tarot directory and assign it as the value of the "past" key of spread.
#
# 3. The second card you draw is card 22. Pop the value assigned to the key 22 out 
# 	 of the tarot dictionary and assign it as the value of the "present" key of
# 	 spread. 
#
# 4. The third card you draw is card 10. Pop the value assigned to the key 10 out 
#    of the tarot dictionary and assign it as the value of the "future" key of spread.
#
# 5. Iterate through the items in the spread dictionary and for each key:value pair, 
# 	 print out a string that says:
#		
#		 Your {key} is the {value} card. 
#
# 6. Congratulations! You have learned about how to modify and use dictionaries. 
#		 Hit the Run button one more time when you are ready to continue. 

# Gonna try make it a bit bigger with random instead of predefined pops. 
import random

tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}


card_one = random.randint(0, len(tarot))
card_two = random.randint(0, len(tarot))
card_three = random.randint(0, len(tarot))

spread = {}

spread["past"] = tarot.pop(card_one)
spread.update({"present": tarot.pop(card_two)})
spread.update({"future": tarot.pop(card_three)})

for time, card in spread.items():
	print("Your " + time + " is the " + card + " card.")


# BOOM! Made it, with my added random factor. 
# First tested on myself:
# Past: The Chariot
# Present: The Hanged Man
# Future: The Fool
# I want to beleive this, it feels fitting :D 

# Cheers!


