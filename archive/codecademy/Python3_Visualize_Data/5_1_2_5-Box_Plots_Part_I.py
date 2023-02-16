# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 5. Box Plots, Part I

'''
While a KDE plot can tell us about the shape of the data, it's cumbersome to compare
multiple KDE plots at once. They also can't tell us other statistical information,
like the values of outliers.

The box plot (also known as a box-and-whisker plot) can't tell us about how our 
dataset is distributed, like a KDE plot. But it shows us the range of our dataset,
gives us an idea about where a significant portion of our data lies, and wheter 
or not any outliers are present.

Let's examine how we interpret a box plot:

- The box represents the interquartile range
- The line in the middle of the box is the median
- The end lines are the first and third quartiles
- The diamonds show outliers

'''

# see 5_1_2_5-fig.svg