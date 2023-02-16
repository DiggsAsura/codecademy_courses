# 7. Specialized Collections
# 1. Sets
# 11. Symmetric Difference

print('\nSymmetric Difference\n-------------------')

# The last operation we will be looking at is the symmetric difference. We can
# can think of this operation as the opposite of the intersection operation. 
# A resulting set will include all elements from the sets which are in one or
# the other, but not both. In other words, elements that are unique to each
# set.
#
# To perform this operation on the set or frozenset containers, we can use the 
# .symmetric_difference() method or the ^ operator. Like the other operators,
# the type of the first operant (a set or forzenset) determines if a set or
# frozenset is returned when finding the symmetric difference.
#
# Take a look at the Venn diagram that represents a symmetric difference
# between set A and set B:

# <fig symmetric_difference> 
# Two crossing cricles, where the non-crossing part on both circles are 
# colored. Means it's all the uniques. 

# Here is what the symmetric difference looks like in Python:

preparey_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}
py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

exclusive_tags = preparey_to_py.symmetric_difference(py_and_dry)
print(exclusive_tags)

frozen_exclusive_tags = py_and_dry ^ preparey_to_py
print(frozen_exclusive_tags)

# We can also update the original set using this operation by using the
# .symmetric_difference_update() method to update the original set with the
# result instead of returning a new set or frozenset object.


print('\nTasks\n----------')

# 1. The users of our app would like to be able to see which tags are unique
#    between them and their friends. This means that the tags which are not
#    shared between the user and their friend are shown. In order to find this,
#    we can use the symmetric difference.
#
#    First, create a set called user_tags.
#
#    Use a loop to populate the set to contain all the tags from the songs
#    in user_song_history
#
# 2. Next, repeat the same logic in order to collect all of the tags from the
#    friend_song_history and store it in a set called friend_tags.
#
# 3. Finally, find the unique tags by getting the symmetric differene between
#    user_tags and friend_tags.
#
#    Store the result in a set called unique_tags and then print it!

user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}


user_tags = set()
friend_tags = set()


for key, value in user_song_history.items():
  for tag in value:
    user_tags.add(tag)

for key, value in friend_song_history.items():
  for tag in value:
    friend_tags.add(tag)

unique_tags = user_tags ^ friend_tags # apparently had to be below the for loops.

print(f"User tags: {user_tags}")
print(f"Friend tags: {friend_tags}")

print(f"A collection of unique tags when comparing user and friend tags: {unique_tags}")