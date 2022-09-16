# Tasks given is to create a nested loop to print out value of the two dimensional list

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
	print(location)

	for i in location:
		# Failed a few times on order here. It's important!
		scoops_sold += i
		#print(i)

print(scoops_sold)


