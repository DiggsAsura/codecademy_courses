# 7. Specialized Collections
# 1. Sets
# 8. Set Union

print('\nSet Union\n---------')

# When working with set or frozenset container, one of the most common 
# operations we can perform is a merge. To do this, we can return the union of 
# two sets using the .union() method or | operator. Doing so will return a new
# set or frozenset containing all elements from both sets without duplicates.
#
# Take a look at the Venn diagram representing a union of set A and set B:
#
# figure
#
# Notice the resulting set contains all the elements in both set A and set B as
# well as elements they have in common (minus the duplicates). In this case we
# are only looking at merging two sets but it's also common to perform the 
# operation on as many as we need!
#
# Let's look at two examples of creating a union:

# 1. Using union()
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})
combined_tags = prepare_to_py.union(py_and_dry)
print(combined_tags)
#! Output:
#! {'rock and roll', 'heavy metal', 'electric guitar', 'classic', 'rock', 'synth'}

# 2. using |
frozen_combined_tags = py_and_dry | prepare_to_py
print(frozen_combined_tags)
#! Output:
#! frozenset({'heavy metal', 'rock', 'classic', 'synth', 'rock and roll', electric guitar'})

# Note that the return value in both methods take the form of the left operand.
# In the first example since prepare_to_py() called the union() function, so
# the result was a regular set. In the second example, since py_and_dry was
# the left operand, the end result was a frozenset. 


print('\nTasks\n----------')

# 1. To Improve the logic for adding user tags to songs in the app, we can use 
#    the union of tag sets! Our team has provided us two dictionaries.
#
#    The first dictionary (song_data) contains song data including tags from
#    the original artists, while the second dictionary (user_tag_data) 
#    includes tags that have been added by users. Let's attempt to merge the tag
#    sets together so we have a full collection of tags. 
#
#    First, create an empty dictionary called new_song_data which will hold
#    the merged tag data.
#
# 2. Our goal now is to consolidate the tags into one dictionary for each
#    category. To accomplish this we need to:
#
#    - Loop over song_data.items() (all the items in song_data)
#
#       - On each iteration of the loop, create a set for each category of 
#         tags. This will require creating two new sets, one for song_data
#         and one for user_tag_data.
#
#       - In addition to creating the sets on each iteration, create a new
#         key inside of new_song_data for each category and set the value to
#         be a union of the two new sets.
#
#    Print new_song_data to see the result!

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}


new_song_data = {}

for key, value in song_data.items():
  song_tag_set = set(value)
  user_tag_set = set(user_tag_data[key])
  new_song_data[key] = song_tag_set | user_tag_set

print(new_song_data)

# Had to read up the for loop. Too tired. 