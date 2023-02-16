# Chapter 6 - Python Code Challenges
# Loops (Advanced) 2
# Over 9000

# We are constructing a device that is able to measure the power level of our coding abilities and 
# according to the device, it will be impossible for our power levels to be over 9000. Because of this,
# as we iterate through a list of power values we will count up each of the numbers until our sum reaches
# a value greater than 9000. Once this happens, we should stop adding the numbers and return the value
# where we stopped. In order to do this, we will need the following steps:

# 1. Define the function to accept a list of numbers
# 2. Create a variable to keep track of our sum
# 3. Iterate through every element in our list of numbers
# 4. Within the loop, add the current number we are looking at to our sum
# 5. Still within the loop, check if the sum is greater than 9000. If it is, end the loop
# 6. Return the value of the sum when we ended our loop

# Ok this is motivating. It's a bit difficult, but I like it. Let's see how it goes. 

#def over_nine_thousand(lst):
	#sum = 0
	#for num in lst:
	#	sum += num
	#	if sum > 9000:
	#		return sum
	#		break
	#	else:
	#		return sum
	
	#return sum
	
	# I overdid the above quite a bit. It was close tho, just simplifie it a bit more!
	
def over_nine_thousand(lst):
	sum = 0
	for num in lst:
		sum += num
		if (sum > 9000): 
			break
	return sum
	
	
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
