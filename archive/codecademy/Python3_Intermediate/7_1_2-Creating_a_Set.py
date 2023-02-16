# 7. Specialized Collections
# 1. Sets
# 2. Creating a Set

print('\nCreating a Set -----\n')
# In Python, there are multiple ways to create a set. A set object can be created
# by passing an iterable object into its constructor, using curly braces, or using
# a set comprehension.
#
# Let's examine the syntax of these methods:

#!# Creating a set with curly braces
music_genres = {
  'county',
  'punk',
  'rap',
  'techno',
  'pop',
  'latin'
}

#!# Creating a set from a list using set()
music_genres_2 = set(['country', 'punk', 'rap', 'techno', 'pop', 'latin'])

# It's worth noting that creating a set from a list with duplicates produces
# a set with the duplicates removed. Here is an example:

#!# Creating a set with curly braces:
music_genres_3 = set(['country', 'punk', 'rap', 'pop', 'pop', 'pop'])
print(music_genres_3)

#!# Output:
#!# {'country', 'punk', 'pop', 'rap'} # in assorted order

# While we use similar data type in the sets above, sets can actually contain any
# combination of data types as long as they are unique values. Here is an example:

music_different = {70, 'music times', 'categories', True, 'country', 45.7}

# We can also create an empty set with one specific method:

#!# Creating an empty set using the set() constructor
#!# Doing set = {} will define a dictionary rather than a set
empty_genres = set()

# Lastly, similar to list comprehensions, we can create sets using a set
# comprehension and a data set (such as a list). Here is an example:

items = ['country', 'punk', 'rap', 'techno', 'pop', 'latin']

music_genres_4 = {category for category in items if category[0] == 'p'}
print(music_genres_4)

# Would output a set containing all elements from items starting with the 
# letter 'p':

#!# {'punk', 'pop'}

# Now, let's practice these methods to get a feel of how to create a set!

print('\nTasks ----- \n')
#
# 1. We have a great idea for an application that allows users to share 
#    music that they create with others. 
#
#    One of the features of this application is the ability to tag songs with
#    destriptive tags about the genre, mood, instruments, etc. Our team 
#    members have taken a survey of user's favorite genres of music and 
#    provided us with a list of the results.
#
#    Unfortunatly, it seems like there are some duplicates in the collection.
#    For the first step, find all the genres of music that the users submitted
#    without duplicates by creating a set from genre_results.
#
#    Store the set in a variable called survey_genres. Finally, print
#    survey_genres to see the new set!
#
# 2. You want to test if it is plausible to use abbreviated tags for 
#    describing music.
# 
#    For this step, use a set comprehension to create a new set called
#    survey_abbreviated which stores the first three letters of each 
#    genre found in the survey results without duplication.
#
#    Print survey_abbreviated to see the result!

genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

survey_genres = set(genre_results)
print(survey_genres)

survey_abbreviated = {item[:3] for item in survey_genres}
print(survey_abbreviated)

# Ok motivation is back. These small understandable tasks is better then
# some of the projects lol. 