# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 11. Figures

'''
When we're making lots of plots, it's easy to end up with lines that have been
plotted and not displayed. If we're not careful, these "forgotten" lines will
show up in your new plots. In order to be sure that you don't have any stray
lines, you can use the command plt.close('all') to clear all existing plots
before you plot a new one.

Previously, we learned how to put two sets of axes in the same figure. Sometimes,
we would rather have two separate figures. We can use the command plt.figure()
to create new figures and size them how we want. We can add the keyword 
figsize=(width, height) to set the size of the figure, in inches. We use 
parantheses () to pass in the witdh and height, which are separated by a comma.

To create a figure with a diwth of 4 inches, and height of 10 inches, we would 
use:


plt.figure(figsize=4, 10))


It would look tall and skinny.

Once we've created a figure, we might want to save it so that we can use it in
a presentation or a website. We can use the command plt.savefig() to save
out to many different file formats, such as png, svg or pdf. After plotting,
we can call plt.savefig('name_of_graph.png'):


plt.figure(figsize=(4, 10))
plt.plot(x, parabola)
plt.savefig('tall_and_narrow.png')

'''

from matplotlib import pyplot as plt

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')

plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word.lengths.png')
plt.show()

plt.figure(figsize=(7,3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')
plt.show()