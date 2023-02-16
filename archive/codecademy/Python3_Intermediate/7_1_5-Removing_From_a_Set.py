# 7. Specialized Collections
# 1. Sets
# 5. Removing From a Set

print('\nRemoving From a Set\n---------------')

# There are two methods for removing specific elements from a set:
#
# 1. The .remove() method searches for an element within the set and removes
#    if it exists, otherwise, a KeyError is thrown.

song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}

song_tags.remove('folk')
print(song_tags)

#!# Try removing a non-existent element
#!#song_tags.remove('fiddle')  # --> KeyError

#!# Would output:
#!# {'blues', 'acoustic', 'country', 'guitar', 'live'}

# 2. The .discard() method works the same way but does not throw an exception
#    if an element is not present.

song_tags.discard('guitar')
song_tags.discard('fiddle')
print(song_tags)

#!# Would output:
#!# {'folk', 'acoustic', 'blues', 'live', 'country'}

# Note that items cannot be removed from a frozenset so neither of these
# methods would work. 

print('\nTasks\n-------')

# 1. Some users have created tags that are not related to music, and you'd 
#    like to get rid of them. For now, let's manually remove the incorrect
#    tags. 
#
#    To start off, we need another set for the tag data within 
#    song_data_users. Create a set called tag_set and store the tag data
#    for 'Retro Words'
#
# 2. Now we need to remove the tags which are unrelated to music. In this 
#    case, remove the tags: 'onion', 'helloworld', and 'spam'.
#
# 3. For the last step, replace the value of the key, 'Retro Words' inside
#    of song_data_users so that it is equal to the updated tag set.
#
#    Print song_data_users to see the results. 

song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

tag_set = set(song_data_users['Retro Words'])

# Can use .discard or .remove
tag_set.discard('onion')
tag_set.remove('helloworld')
tag_set.discard('spam')

song_data_users = {'Retro Words': tag_set}

print(song_data_users)

# Note that the song_data_users dictionary value initially is a list. 
# The value gets changed to a set, which also uses {} after the modification.
