# Chap 7.2 - Strings
# String Methods
# 13. Review

# Ok time to sum up. 

# .upper(), .title() and .lower() adjust the casing
# .split() creates a list of substrings (based on deliminator)
# .join() takes a list of strings and creates a string
# .strip() removes whitespaces, or char based on deliminator supplied, from the beginning and end 
# .replace() replaces all instances of a character/string with another char/string
# .find() searches a string for a character/string and returns the index value of where that char/string starts
# .format() allows you to interpolate a string with variables

# Task: 
# 1. First, start by printing highlighted_poems to the terminal and see how it displays
# 2. Start by splitting highlighted_poems at the commas and save it to highlighted_poems_list
# 3. Print highlighted_poems_list, how does the structure of the data look now?
# 4. Create highlighted_poems_stripped list, then iterate through highlighted_poems_list and strip
#    away the whitespace and append it to your new list, highlighted_poems_stirpped
# 5. Print highlighted_poems_stripped. Looks good! All whitespace is cleaned up
# 6. Next we want to break up all the information for each poem into it's own list, so we 
#    end up with a list of lists.
#    Create a new empty list called highlighted_poems_details.
# 7. Iterate through highlighted_poems_stripped and split each string around the : characters and
#    append the new lists into highlighted_poems_details
# 8. Great! Now we want to separate out all of the titles, the poets, and the publication dates into their 
#    own lists. 
#    Create three new empty lists, titles, poets and dates
# 9. Iterate through highlighted_poems_details and for each list in the list append the appropriate elements 
#    into the lists titles, poets and dates
# 10. Finally, write a for loop that uses .format() to print out the following string for each poem: 
#     The poem TITLE was published by POET in DATE.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

print("\n")
print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
	highlighted_poems_stripped.append(poem.strip())

print("\n")
print(highlighted_poems_stripped)

highlighted_poems_details = []
for poem in highlighted_poems_stripped:
	highlighted_poems_details.append(poem.split(":"))

print("\n")
print(highlighted_poems_details)

titles = []
poets = []
dates = []
for i in highlighted_poems_details:
	titles.append(i[0])
	poets.append(i[1])
	dates.append(i[2])

print("\n")
for i in range(len(titles)):
	print("The poem {title} was published by {poet} in {date}.".format(title=titles[i], poet=poets[i], date=dates[i]))


# Ok sweet, got it all. Had to look up a bit of hint on part 10 only, but it makes perfect sense and I did figure
# since they all have the same indices, we should only have to iterate through one list. 



