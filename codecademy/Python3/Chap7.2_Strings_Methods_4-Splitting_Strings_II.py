# Chap 7.2 - Strings
# String Methods
# 4. Splitting Strings II

# Okies so now we are moving into the deliminator (argument). Great!
# Consider this example:
"""
greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))
==> ['sa', 'ta', 'a']
"""
# So it will just define where to split. Also, does not include the letter we chose to split from.

# Next example is the same, but with "a" as deliminator
# this will, and it's normal, end with a empty string at the end
# ==> ['s', 'nt', 'n', ' ']

# 1. Using .split() and the provided string, create a list called author_names containing each individual 
#    author name as it's own string
# 2. Create another list called author_last_names that only contains the last names of the poets in the provided string

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

# Ok second part is not just using .split() - also have to iterate through them and then use split and append into something new.

author_last_names = []
for author in author_names:
	new_lst = author.split()
	author_last_names.append(new_lst[-1])

print(author_last_names)

# Omg yeaaaaa! Got it down on my own, no looking up. I think I do start to go somewhere wooooo!
# This is great fun!
