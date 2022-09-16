# Chap 7 - Strings
# 12. Review

#  
# A little summary of what we been through:
# *** A string is a list of charcacters
# *** A character can be selected from a string using its index string_name[index]. These indicies start at 0. 
# *** A 'slice' can be selected from a string. These can be between two indices or can be open-ended, selecting all of the
#     string from that point.
# *** Strings can be concatenated to make larger strings
# *** len() can be used to determine the number of characters in a string.
# *** Strings can be iterated through using for loops.
# *** Iterating through strings opens a huge potential for applications, especially when combined with conditional statements.
#

# So for the test
# 1. Create two functions, username_generator and password_generator
#    username_generator takes two inputs first_name and last_name, returns username which is a slice of the first three letters
#    from first and the four first from the last name. If the name is shorter, should use full. 
# 2. The password should take the username and shift all the chars one slot to the right. The first char should end up in the 
#    last slot. 
# 3. Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username)
#    To shift the letters right, at each letter the for loop should add the previous letter to the string password.

def username_generator(first_name, last_name):
	return first_name[:3] + last_name[:4]
	
def password_generator(username):
	#return username[1:] + username[0] # this is correct for step 2, but not 3
	password = ""
	for i in range(0, len(username)):
		password += username[i-1]
	return password
	
# Had to look up step 3. Im apparently not confident in range() yet. It should make a list out of all the chars, but is it
# really needed? Guess it is?
# Also see that the solution for step 1 is actually different then mine. Mine would fail if the name was too short. The 
# solution basically just says to have if first_name/last_name < X return full else, what i returned. Not gonna bother with it
# as this makes sense. 
# Get more confident with range()


		
