# 7. Specialized Collections
# 1. Sets
# 6. Finding Elements in a Set

print('\nFinding Elements in a Set\n--------------------')

# In Python, set and frozenset items cannot be accessed by a specific index.
# This is due to the fact that both containers are unordered and have no
# indicies. However, like most other Python containers, we can use the in
# keyword to test if an element is in a set or forzeonset.
#
# Here are some examples of finding if elements exist in a set 
# and frozenset:

song_tags = {'guitar', 'acoustic', 'folk', 'country', 'live', 'blues'}
print('country' in song_tags)
#! Would output:
#! True

# This also works for frozenset:

frozen_tags = frozenset(song_tags)
print('rock' in song_tags)
#! Output:
#! False

# Let's use the in keyword to work with more user tags in our music application!


print('\nTasks\n-----------')

# 1. Now that we have learned about using the in keyword for set containers, we
#    have decided to update the tagging system by automatically removing unrelated
#    tags. 
#
#    Our team members are working on a CSV file containing all allowed keywords,
#    but for now, we will be using a list of allowed words when programming your
#    logic.
#
#    To start, store the tag data from song_data_users into a set called
#    tag_set
#
# 2. Next, we want to capture all of the tags in tag_set that don't belong.
#    Create a list called bad_tags. Then, iterate through each element of 
#    tag_set, adding tags to bad_tags that don't belong.
#
# 3. Now, let's remove all the incorrect tags from tag_set.
#
#    Using the collected bad_tags, write another loop to iterate over each of
#    the tags in bad_tags, and remove the elements from tag_set so we have
#    only the allowed tags.
#
# 4. Finally, replace the value of the key, 'Retro Words" inside of song_data_users
#    so that it is equal to the updated tag set.
#
#    Print song_data_users to see the result.

allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']
song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

tag_set = set(song_data_users['Retro Words'])

bad_tags = {tag for tag in tag_set if tag not in allowed_tags}

for tag in bad_tags:
  if tag in tag_set:
    tag_set.remove(tag)

song_data_users = {'Retro Words': tag_set}

print(song_data_users)