# 7. Specialized Collections
# 1. Sets
# 4. Adding to a Set

print('\nAdding to a Set\n----------------')

# There are two differnet ways to add elements to as set:
#
#   1. The .add() method can add a single element to a set.

song_tags = {'country', 'folk', 'acoustic'}

song_tags.add('guitar')
song_tags.add('country')

print(song_tags)

#!# Output
#!# {'country', 'folk', 'acoustic', 'guitar'}

# 2. The .update() method can add multiple elements.

# Add more tags using a hashable object (such as a list of elements)
other_tags = ['live', 'blues', 'acoustic']
song_tags.update(other_tags)

print(song_tags)

#!# Output
#!# {'acoustic', 'folk', 'country', 'live', 'blues'}

# There are a few things to note about adding to a set:
#
#   - Neither of tehse methods will add a duplicate item to a set.
#
#   - A frozenset can not have any items added to it and so neither of these
#     methods will work.
#
#   - Notice that when the elements are printed, they are not printed in the 
#     same order in which they entered the set. This is because set and 
#     frozenset containers are unordered.
#
# Let's practice adding to a set!


print('\nTasks\n-------')
# 1. In our application, we have a section for upcoming artists to upload 
#    their own music. When uploading songs, the artists add their own tags, but
#    others users can add tags to the songs later on.
#
#    For this version of the app, we are provided a song_data dictionary
#    as well as a few tags from users in the form of strings.
#
#    For the first step, create a new set called tag_set from the original
#    song's tags located in song_data.
#
# 2. Next, add the three user tag strings to tag_set.
#
# 3. Finally, update song_data so that the value of the key, 'Retro Words',
#    is equal to the updated tag set.


song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

tag_set = set(song_data['Retro Words'])
print(tag_set)

tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

# or tag_set.update([user_tag_1, user_tag_2, user_tag_3])

song_data = {'Retro Words': tag_set}

print(song_data)