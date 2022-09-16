# Task is to print out everyt age above 21

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
	if i >= 21:
		print(i)
		continue
	# Following is personal testing. Not the expected output: Thought it would just list out the underage, but hey this works too.
	elif i < 21:
		print(i, ": Come back when you're old enough!")


