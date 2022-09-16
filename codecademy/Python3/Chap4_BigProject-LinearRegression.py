# Ok first project to try incorporate everything we have learend
# so far. To be honest, this one, imo, just turned everything up 10 
# notches and i dont really understand much of whats going on. At this
# point it is kind of demotivating, but I'll try power through!

# We also start using jupyter notebook. Not sure if I like it, yet. Much prefer
# a small editor like gedit on my Debian-box. 

# Project: Linear Regression

# Part 1: Calculating Error
# The formula should be
# y = m*x + b

# m is the slope of the line and b is the intercept, where the line crosses
# the y-axis

def get_y(m, b, x):
	y = m*x + b
	return y
	
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


def calculate_error(m, b, point):
	x_point, y_point = point
	y = m*x_point + b
	distance = abs(y - y_point)
	return distance

# this is a line that looks like y = x, so (3, 3) should lie on it
# i can't really comprehend what the task is telling me lol gdi
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1,1, (3, 3)))



datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

def calculate_all_error(m, b, datapoints):
	total_error = 0
	for point in datapoints:
		point_error = calculate_error(m, b, point)
		total_error += point_error
	return total_error
	
#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))


#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))



# nope, this is way above my head!

possible_ms = [m * 0.1 for m in range(-10, 11)]
possible_bs = [b * 0.1 for b in range(-20, 21)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs: 
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error
            
print(best_m, best_b, smallest_error)

ex1 = get_y(0.3, 1.7, 6)
print(ex1)

ex2 = get_y(2.2, 2.1, 15)
print(ex2)


# I probably have to read over this several times to try digest it. I think Codecademy 
# went a bit far with this project. From tiny lessons to this big one with linear regression
# Hope its not only me that was overwhelmed by this one!
# Will keep pushing on tho!!


