# 7. Specialized Collections
# 1. Sets
# 12. Sets Review

print('\nSets Review\n-----------------')

# Great job! You have learned about the many of the different ways to work with set 
# and frozenset containers! We looked at:
#
# Createing set and frozenset:
#
#   - For set containers, we can use curly braces {}, the set() constructor,
#     or set comprehension.
#
#   - For frozenset containers, we can use only the frozenset() constructor.
#
# Adding items to a set:
#
#   - We can add items to a set individually using the .add() method.
#
#   - We can add multiple items at once using the .update() method.
#
# Removing items from a set:
#
#   - The .remove() method is used to remove elements from a set.
#
#   - The .discard() method can also be used to remove elements from a set. It
#     does not throw a KeyError if the element is not found.
#
# Finding Elements:
#
#   - The in keyword can be used with set and frozenset containers to test if
#     an element exists inside of them.
#
# *Union:
#
#   - A union can be found using set or frozenset containers with the .union()
#     method or | operator.
#
# *Intersection:
#
#   - An intersection can be found using set or frozenset containers with the 
#     .intersection() method or the & operator.
#
# *Difference:
#
#   - The difference can be found using set or frozenset containers with the 
#     .difference() method or - operator.
#
# *Symmetric Difference:
#
#   - The symmetric difference can be found using set or frozenset containers
#     with the .symmetric_difference() method or ^ operator.
#
# Want to learn more about sets? Check out everything about sets including
# additional methods, testing for superclass and subclasses, and more from
# the Python documentation:
# https://docs.python.org/3/library/stdtypes.html#set


print('\Tasks\n -------------')

# 1. For these checkpoints, we will review the different operations which you 
#    can perform on set and frozenset containers.
#
#    First, create a frozenset called my_tags which contains the elements:
#    'pop', 'electronic', 'relaxing', 'slow' and 'synth'.
#
# 2. Try finding the union of music_tags and my_tags, but make sure to return
#    the result as a frozenset. Store the result in a variable called
#    frozen_tag_union.
#
# 3. Now store the intersection of music_tags and my_tags into a variable 
#    called regular_tag_intersect. Make sure that it is stored as a normal
#    set this time.
#
# 4. Now try finding the difference of my_tags with music_tags. Store this result
#    in a variable called frozen_tag_difference. The type of the result should
#    be a frozenset.
#
# 5. Finally, get the symmetric difference of music_tags with my_tags and store
#    it in a variable called regular_tag_sd. The result should be a set
#    and not a frozenset.


music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}
my_tags = frozenset({'pop', 'electronic', 'relaxing', 'slow', 'synth'})

frozen_tag_union = my_tags | music_tags
regular_tag_intersect = music_tags & my_tags
frozen_tag_difference = my_tags - music_tags
regular_tag_sd = music_tags ^ my_tags


# Easiset review ever :)