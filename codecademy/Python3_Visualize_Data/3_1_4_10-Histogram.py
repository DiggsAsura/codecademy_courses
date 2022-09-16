# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 10. Histogram

'''
Sometimes we want to get a feel for a large dataset with many samples beyond
knowing just the basic metrics of mean, median or standard deviation. To get
more of an intuitive sense for a dataset, we can use a histogram to display all
the values.

A histogram tells us how many values in a dataset fall between different sets of
numbers (i.e, how many numbers fall between 0 and 10? Between 10 and 20? Between
20 and 30?). Each of these questions represents a bin, for instance, our first
bin might be between 0 and 10.

All bins in a histogram are always the same size. The width of each bin is the
distance between the minimum and maximum values of each bin. In our
example, the width of each bin would be 10.

Each bin is represented by a different rectangle whose height is the number of
elements from the dataset that fall within that bin.

Here is an example:

<fig not here, sorry. Looking like a siluette of a city center>

To make a histogram in Matplotlib, we use the command plt.hist(). plt.hist()
finds the minimum and the maximum values in your dataset and creates 10 
equally-spaced bins between those values.

The histogram above, for example, was created with the following code:


plt.hist(dataset)
plt.show()


If we want more than 10 bins, we can use the keyword bins to set how many bins
we want to divide the data into. The keyword range selects the minimum and 
maximum values to plot. For example, if we wanted to take our data from the 
last example and make a new histogram that just displayed the values from 66 to
69, divided into 40 bins (instead of 10), we could use this function call:


plt.hist(dataset, range=(66, 69), bins=40)


which would result in a histogram that looks like this:


<no fig...> 


Histogram are best for showing the shape of a dataset. For example, you might 
see that values are close together, or skewed to one side. With this added
intuition, we often discover other types of analysis we want to perform.

'''

# This included sales_times.csv and a script-3_1_4_10.py

from matplotlib import pyplot as plt
from script_3_1_4_10 import sales_times

plt.hist(sales_times, bins=20)

plt.show()