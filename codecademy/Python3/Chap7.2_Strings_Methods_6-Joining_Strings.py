# Chap 7.2 - Strings
# String Methods
# 6. Joining Strings

# Learning .join() which basically is the opposite of split(). It joins a list of strings toegher with a given delimiter.
"""
delimiter.join(list_you_want_to_join)
"""
# Now this may seem a little weird, because with .split() the arguments was the delimiter, but now the argument is the list.
# This is because join is still a string method, which means it has to act on a string. The string .join() acts on is the 
# delimiter you want to join with, therfor the list you want to join has to be the argument.
#
# This can be a bit confusing, so let's take a look at an example.
"""
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
==> 'My Spanish Harlem Mona Lisa'
"""
# We take the list of strings, my_munequita, and we joined it together with our delimiter ' ' which is a space. The space is 
# important if you are trying to build a sentence from words, otherwise, we would have ended up with:
"""
print(''.join(my_munequita))
==> 'MySpanishHarlemMonaLisa'
"""
# Okies that makes sense. 

# 1. You've been provided with a list of words from the first line of Jean Toomer's poem Reapers.
#    Use .join() to combine these words into a sentence and save that sentence as the string reapers_line_one

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = (' '.join(reapers_line_one_words))
print(reapers_line_one)
