# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 11. Multiple Histograms

'''
If we want to compare two different distrubutions, we can put multiple histograms
on the same plot. This could be useful, for example, in comparing the heights
of a bunch of men and the heights of a bunch of women. However, it can be hard
to read two histograms on top of each other. For example, in this histogram, 
we can't see all of the blue plot, because it's covered by the orange one:


<fig with overlapping histograms>


We have two ways we can solve a problem like this:

1. use the keyword alpha, which can be value between 0 and 1. This sets the 
   transparency of the histogram. A value of 0 would make the bars entirely
   transparent. A value of 1 would make the bars completly opaque.
   
   plt.hist(a, range(55, 75), bins=20, alpha=0.5)
   plt.hist(b, range(55, 75), bins=20, alpha=0.5)

2. use the keyword histtype with the argument 'step' to draw just the outline
   of a histogram:
   
   plt.hist(a, range=(55, 75), bins=20, histtype='step')
   plt.hist(b, range=(55, 75), bins=20, histtype='step')
   
   <fig just the skeleton/outline>

Another problem we face is that our histograms might have different numbers of 
samples, making one much bigger than the other. We can see how this makes it
difficult to compare qualitatively, by adding a dataset b with a much bigger
size value:


a = normal(loc=64, scale=2, size=1000)
b = normal(loc=70, scale=2, size=10000)

plt.hist(a, range=(55, 75), bins=20)
plt.hist(b, range=(55, 75), bins=20)
plt.show()


The result is two histograms that are very difficult to compare:

<fig one super low and the other very tall>

To solve this, we can normalize our histograms using normed=True. This command
divides the height of each column by a constant such that the total shaded
area of the histograms sums to 1.


a = normal(loc=64, scale=2, size=1000)
b = normal(loc=70, scale=2, size=10000)

plt.hist(a, range=(55, 75), bins=20, alpha=0.5, normed=True)
plt.hist(b, range=(55, 75), bins=20, alpha=0.5, normed=True)
plt.show()


Now, we can more easily see the differences between the blue set and the 
orange set.

<fig two about same height figures. But did i understand this one..?> 

'''

from matplotlib import pyplot as plt
from script_3_1_4_11 import sales_times1
from script_3_1_4_11 import sales_times2

plt.hist(sales_times1, bins=20, alpha=0.4) # normed=True fails 
#plot your other histogram here
plt.hist(sales_times2, bins=20, alpha=0.4)

plt.show()