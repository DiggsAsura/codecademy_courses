# 7. Specialized Collections
# 1. Sets
# 9. Set Intersection

from sys import set_asyncgen_hooks


print('\nSet Intersection\n------------')

# Let's say that we have two or more sets, and we want to find which items both
# sets have in common. The set container has a method called .intersection()
# which returns a new set or frozenset consisting of those elements. An
# intersection can also be performed on multiple sets using the & operator.
#
# Similar to the other operations, the type of the first operand (a set of a
# frozenset on the left side of the operator or method) determines if a set or 
# frozenset is returned when finding the intersection.
#
# Take a look at the Venn diagram representing an intersection of set A and
# set B
#
# <Figure> Two circles crossing with the crossing part highlighted
#
# Here is what an intersection looks like in Python:

prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

frozen_intersected_tags = py_and_dry.intersection(prepare_to_py)
intersected_tags = prepare_to_py.intersection(py_and_dry)

print(frozen_intersected_tags)
print(intersected_tags)

#! Output
#! frozenset({'electric guitar', rock})
#! {'rock', 'electric guitar'}

# In addition to a regular intersection, the set container can also use a method
# called .intersection_update(). Instead of returning a new set, the original
# set is updated to contain the result of the intersection.
#
# Let's see how we can use the intersection operation to create a 
# recommendation feature for our music application!


print('\nTasks\n----------')

# 1. We want to add a feature to our app which will reccomend songs based on the
#    most recent songs a user has listened to. One way we can do this is by
#    using the intersection of the recent song tags. Let's use the intersection
#    of these tags to find which other songs are similar.
#
#    First, create a variable called tags_int that stores the intersection
#    between the tags for the user_recent_songs two recent songs 'Retro Words'
#    and 'Lowkey Space'. Remember to convert each list into a set to 
#    perform the operation.
#
#    We will be using these common tags as a basis for finding a recommended
#    song in song_data.
#
# 2. Now, let's find the recommended song based on the common tags we found
#    in the previous step.
#
#    Find all the other songs in song_data which have these tags. Store the
#    songs which have any matching tags into a dictionary called 
#    recommended_songs. Make sure that you do not add any songs which the
#    user has listened to recently!
#
#    Print recommended_songs to see the result!

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}


tags_int = set(user_recent_songs['Retro Words']) & set (user_recent_songs['Lowkey Space'])
print(tags_int)

recommended_songs = {}

for key, value in song_data.items():
  for tag in value:
    if tag in tags_int:
      if key not in user_recent_songs:
        recommended_songs[key] = value

print(recommended_songs)