# 7. Specialized Collections
# 1. Sets
# 10. Set Difference

print('\nSet Difference\n--------------')

# Similar to how we can find elements in common between sets, we can also find
# unique elements in one set. To do so, the set or forzenset use the .difference()
# method or the - operator. This returns a set or frozenset, which contains
# only the elements from the first set which are not found in the second set.
# Similar to the other operations, the type of the first operand (a set or
# a frozenset on the left side of the operator or method) determines if a set
# or frozenset is returned when finding the difference.
#
# Take a look at the Venn diagram representing a difference operation that
# captures elements that are unique to set A:

# <fig difference()>
# Two crossing circles (A and B), where the unique part of A is is colored

# Here is what finding a set difference looks like in Python:

prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

only_in_prepare_to_py = prepare_to_py.difference(py_and_dry)
only_in_py_and_dry = py_and_dry - prepare_to_py
print(only_in_prepare_to_py)
print(only_in_py_and_dry)

# This operation also supports an updating version of the method. You can use
# .difference_update() to update the original set with the result instead of
# returning a new set or frozenset object.
#
# Let's see how we can apply this operation to our music application!

print('\nTasks\n-----------')

# 1. In order to try and increase the accuracy of your app's song recommendations,
#    we have decided to add some logic that will find the differences between
#    liked and disliked songs. We will create another recommended dictionary of
#    songs based on these differences.
#
#    Create a new variable called tag_diff that is the set difference between 
#    the tags inside of the one song of user_liked_song and the one song of
#    user_disliked_song. Don't forget to convert the list of tags into a
#    set to perform this operation!
#
# 2. Now that you know the difference in tags between the liked song and 
#    disliked song, use those tags to find any songs from song_data which 
#    contain them. 
#
#    Make sure not to include the liked and disliked songs. Store the newly 
#    found songs into a dictionary called recommended_songs.
#
#    Print recommended_songs to see the result!

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

liked = set(user_liked_song['Back To Art'])
disliked = set(user_disliked_song['Retro Words'])

tag_diff = liked.difference(disliked)

# So the confusing part, which I allmost got, but still unclear. Why can't 
# i check if the value is inside the set's? Maybe I can somehow?

recommended_songs = {}

for key, value in song_data.items():
  for tag in value:
    if tag in tag_diff:
      if key not in user_liked_song and key not in user_disliked_song:
        recommended_songs[key] = value

print(recommended_songs)