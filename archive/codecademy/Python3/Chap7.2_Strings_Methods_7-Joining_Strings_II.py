# Chap 7.2 - Strings
# String Methods
# 7. Joining Strings II

# It's gonna be rough remember the syntax for join. Hope I can remember it's the "opposite" then split. 
# aka ' '.join(string) vs string.split(' ')

# 1. You've been given a list, winter_trees_lines, that contains all the lines to William Carlos Williams poem, Winter Trees.
#    You've been asked to join together the strings in the list together into a single string that can be used to display the 
#    full poem. Name this string winter_trees_full
# 
#    Print your result to the terminal. Make sure that each line of the poem appears on a new line in your string. 

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)
