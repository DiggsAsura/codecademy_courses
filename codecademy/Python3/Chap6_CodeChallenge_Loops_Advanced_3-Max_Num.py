# Chapter 6 - Python Code Challenges
# Loops (Advanced) 3
# Max Num

# Here is a more traditional coding problem for you. This function will be used to find the maximum number in a 
# list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going
# to manually implement this function. Here is what we need to do:

# 1. Define the function to accept a list of numbers called nums
# 2. Set our default maximum value to be the first element in the list
# 3. Loop through every number in the list of numbers
# 4. Within the loop, if we find a number greater than our starting maximum, then replace the maxiumum with 
#		 what we found
# 5. Return the maximum number

def max_num(nums):
	defmax = nums[0] # this one i worried, but it is correct
	for num in nums: # correct
		if num > defmax: # correct
			#nums.insert(0, num) # wrong - no insert at all
			defmax = num
	return defmax
	
# I feel this should be really really close. I think it should be insert, as i can place it at 0 (i don't
# think .append can do so). However the intepreter hangs so apparently something is wrong here lolol.

# Ok so the solution was easier then I thought. Makes sense when reading over. 
# Still kinda close tho! 
	
	
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
