# Chapter 6 - Python Code Challenges
# Functions (Advanced) - 3
# Bond, James Bond

# It's time to re-create a famous movie scene through code. Our function is going to concatenate strings 
# together in order to replace James Bond's name with whatever name we want. The input to our function will
# be two strings, one for a first name and another for a last name (maybe I add a third actually). The function
# will return a string consisting of the famous phrase but replaced with our inputs. Two accomplish this, we need
# to: 

# 1. Define the function to accept two parameters, first_name and last_name (i add middle_name too)
# 2. Concatenate the wring ', ' on to the last_name
# 3. Concatenate the first_name on to the result of the previous step
# 4. Concatenate a space on to the result
# 5. Concatenate the last_name again to the result
# 6. Return the final string

# Ok I did this, or at least very similar before. Should be possible to do without any guideance. Will also add
# middle_name, to use my own full name for the lolz. 

def introduction(first_name, middle_name, last_name):
	return last_name + ", " + first_name + " " + middle_name + " " + last_name
	
# Uncomment these function calls to test your introduction function:
print(introduction("Kenneth", "Bæver", "Bjerke"))
# should print Bond, James Bond
print(introduction("Maya", "Bæver", "Angelou"))
# should print Angelou, Maya Angelou

# Major aha when it comes to cocatenate strings. NEEDS to be +, the comma , won't do if you want a readable output!!
