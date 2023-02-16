# Chap 7.2 - Strings
# String Methods
# 5. Splitting Strings III

# Learning about escape sequences. Escape sequences are used to indicate that we want to split something in a string that
# is not necessarily a character. Two covered here:
# \n Newline
# \t Horizontal tab
# \n i know, \t is particular useful when dealing with certain datasets because it's not uncmomon for data points to be 
# separated by tabs. Okies have to dig into that. For now try to remember it.

# Example code: 
smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""
print(smooth_chorus + "\n")

chorus_lines = smooth_chorus.split('\n')
print(chorus_lines)

# This code wrapping every natural line of the smooth-chorus into string "chunks" in a list. 

# Ok for the task at hand: 
# 1. Break the poem into it's individual lines. Create a list called spring_storm_lines that contains a string for each line
# of Spring Storm

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)
