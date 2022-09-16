# Chap 7.2 - Strings
# String Methods
# 8. .strip()

# When working with strings that come from real data, you will often find that the strings aren't super clean.
# You'll find lots of extra whitespcaes, unnecessary linebreaks, and rogue tabs. 
#
# Python provides a great method for cleaning strings: .strip()
# Stripping a string removes all whitespace characters from beginning and end. Consider the following example:
featuring = "       rob thomas                  "
print(featuring.strip())
# ==> 'rob thomas'
# 
# All the whitespace on either side of the string has been stripped, but the whitespace in the middle has been preserved.
# 
# You can also use .strip() with a character argument, which will strip that character from either end of the string.
featuring = "!!!rob thomas        !!!!!"
print(featuring.strip("!"))
# ==> 'ro thomas           '
# By including the argument '!' we are able to strip all tof the ! characters from either side of the string. Notice that now 
# that we've included an argument we are no longer stripping whitespaces, we are ONLY stripping the argument. 

# Task at hand
# 1. They sent over another list containing all the lines to the Audre Lorde poem, Love, Maybe. They want you to join 
#    together all of the lines into a single string that can be used to display the poem again, but this time
#    you've noticed that the list contains a ton of unnecessary whitespaces that doesn't appear in the actual poem. 
#
#    First, use .strip() on each line in the list to remove the unnecessary whitespace and save it as a new list
#    love_maybe_lines_stripped.
#
# 2. .join() the lines in love_maybe_lines_stripped together into one large multi-line string, love_maybe_full, that can
#    be printed to display the poem.
#  
#    Each line of the poem should show up on it's own line.
#
# 3. Print love_maybe_full

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for lines in love_maybe_lines:
	love_maybe_lines_stripped.append(lines.strip())
	
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)
