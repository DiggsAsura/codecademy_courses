# 7. Specialized Collections
# 1. Sets
# 3. Creating a Frozenset

print('\nCreating a Frozenset\n----------------')
# Unlike a normal set, you can only create a frozenset using its constructor.
# Remember that using a frozenset means that you cannot modify the elements
# inside of it.
#
# Creating a frozenset using its constructor looks like this:

#!# Creating a frozenset from a list
frozen_music_genres = frozenset(['country', 'punk', 'rap', 'techno', 'pop', 'latina'])
print(frozen_music_genres)

# We can also create an empty frozenset:

empty_frozen_music_genres = frozenset()

# Let's practice creating a frozenset in our music application!



print('\nTasks\n--------------')
# 1. After calculating the results for the top music genres from the survey,
#    your teammates have sent you a list containing the top three results.
#
#    In order to preserve this data and prevent it from being modified, create
#    a frozenset called frozen_top_genres from the top_genres data. Print our
#    frozen_top_genres to see it!

top_genres = ['rap', 'rock', 'pop']

frozen_top_genres = frozenset(top_genres)

print(frozen_music_genres)