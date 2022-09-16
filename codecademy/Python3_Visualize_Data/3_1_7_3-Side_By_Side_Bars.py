# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 7. Recreate Graphs using Matplotlib
# 3. Side By Side Bars

'''
Now, we are going to look at the chart called side-by-side.png. This displays the
differences in average test scores between students who went to two different middle
schools before enrolling in your high school.

<fig not here>

The data you will need to recreate this chart is in the lists middle_school_a,
middle_school_b and unit_topics.

Save your recreated chart to a file called my_side_by_side.png

'''


from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]


def create_x(t, w, n, d):
  return [t*x + w*n for x in range(d)]

# remember the t w n d 
# t = 2      # There are two sets of data. A and B
# w = 0.8    # Default width
# n = 1      # A is the first set of data
# d = 5      # There are 5 topics we're plotting

school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)

plt.figure(figsize=(10,8))
ax = plt.subplot()

plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)

# Get the tick label in the middle of the two bars
middle_x = [(a+b)/2 for a,b in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

plt.legend(['Middle School A', 'Middle School B'])
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')

plt.savefig('3_1_7_3-side_by_side.png')
plt.show()