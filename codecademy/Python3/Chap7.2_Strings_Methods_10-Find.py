# Chap 7.2 - Strings
# String Methods
# 10. .find()

# At first glance, .find() looks like it will only find the very first placement for whatever we try to find. To
# find all the indices, should make an empty list[] and iterate with a for loop.

# Task:
# 1. In the code editor is the first line of Gabriela Mistral's poem God Wills It. 
#
#    At what index place does the word "disown" appear? Save that index place to the variable
#    diown_placement.

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)
