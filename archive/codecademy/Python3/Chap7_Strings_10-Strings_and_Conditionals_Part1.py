# Chap 7 - Strings
# 10. Strings and Conditionals (Part One)

# Gonna also put in the example here, lesson learned from the previous lesson where they had a quite
# smart example, which was not really tied to the actual task. 

# Count the occurance of a defined letter in a string:

ex_string = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus porta, lacus ac faucibus convallis, mi neque vulputate justo, non vestibulum ex est vitae ex. Quisque dapibus congue dui, quis lobortis velit efficitur eu. Sed risus arcu, euismod nec lacus ac, rhoncus fringilla enim. Mauris et ipsum augue. Aliquam maximus ante elit, a mattis purus tristique vitae. Integer ut erat pulvinar, sodales tellus eleifend, auctor orci. Curabitur ultrices mattis nunc, at vulputate augue varius at. Phasellus blandit consequat ex vel elementum. Pellentesque at tincidunt justo, et fringilla tellus. Donec sed nulla quis ipsum placerat rutrum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Etiam non ornare velit. Duis finibus nec arcu sed maximus. Sed auctor mi vehicula blandit ornare. Nunc odio metus, facilisis a lectus vel, congue vestibulum risus. Donec mauris massa, finibus non venenatis placerat, lacinia vel odio. 
"""

counter = 0
for i in ex_string: 
	if i == "l" or i == "L":
		#counter = counter + 1 # huh wait can't i just counter += 1
		counter += 1 # indeed works. idk wy example did not follow that. 

print(counter)
print(ex_string)
print("")


# The task at hand:
# 1. Write a function called letter_check that takes two inputs, word and letter.
#    This function should return True if the word contains the letter and False if it does not. 

def letter_check(word, letter):
	for i in word:
		if i == letter:
			return True
		else: 
			continue
	return False
	
# the else: continue is totally obsolete. I just had to understand why else: reutnr False didnt work. Got some help
# and figured it out, now it makes total sense, even the indentation placement of return False. Ofc return False will
# never be ran if return True will be ran. 	
	
print(letter_check("ok", "k"))

