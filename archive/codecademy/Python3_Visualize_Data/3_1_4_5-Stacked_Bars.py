# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 5. Stacked Bars

'''
If we want to compare two sets of data while preserving knowledge of the total
between them, we can also stack the bars instead of putting them side by side.
For instance, if someone was plotting the hours they've spent on entertaining 
themselevs with video games and books in the past week, and wanted to also get
a feel for total hours spent on entertainment, they could create a stacked
bar chart:

<fig not here>

We do this by using the keyword bottom. The top set of bars will have bottom set
to the heights of the other set of bars. So the first set of bars is plotted
normally.


video_game_hours = [1, 2, 2, 1, 2]
plt.bar(range(len(video_game_hours)), video_game_hours)


and the second set of bars has bottom specified:


book_hours = [2, 3, 4, 2, 1]
plt.bar(range(len(book_hours)), book_hours, bottom=video_game_hours)


This starts the book_hours bars at the heights of the video_game_hours bars. So,
for example, on Monday the orange bar representing hours spent reading will 
start at a value of 1 instead of 0, because 1 hour was spent playing video 
games.
'''


from matplotlib import pyplot as plt

drinks = ['cappuccino', 'latte', 'chai', 'americano', 'mocha', 'espresso']
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

plt.bar(range(len(sales1)), sales1)
plt.bar(range(len(sales2)), sales2, bottom=sales1)

plt.legend(['Location 1', 'Location 2'])

plt.show()