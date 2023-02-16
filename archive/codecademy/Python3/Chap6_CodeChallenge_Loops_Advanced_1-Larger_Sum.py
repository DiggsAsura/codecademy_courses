# Chapter 6 - Python Code Challenges
# Loops (Advanced) 1
# Larger Sum

# We are going to start our advanced challenge problems by calculating which list of two inputs has the
# larger sum. We will iterate through each of the list and calculate the sums, afterwards
# we will compare the two and return which one has a greater sum. Here are the steps we need:

# 1. Define the function to accept two input paramters: lst1 and lst2
# 2. Create two variables to record the two sums
# 3. Loop through the first list and add up all of the numbers
# 4. Loop through the second list and add up all of the numbers
# 5. Compare the first and second sum and return the list with the greater sum

# Hmm i got some hunches but i dont't see it perfectly clear. Might have to do some trial and error here..

def larger_sum(lst1, lst2):
	sum1 = 0
	sum2 = 0
	for num1 in lst1:
		sum1 += num1
	for num2 in lst2:
		sum2 += num2
	
	if sum1 >= sum2:
		return lst1
	else:
		return lst2
		
	# WEEELLL the function returned the number I wanted, however that was not what the lesson wanted lol. They 
	# apparently ask for a list in return
	# larger_sum([1, 9, 5], [2, 3, 7]) should have returned [1, 9, 5], and it returned 15
	# But god dam I'm so slow today. It literally say return the list, not the sum.. lol. Wake up, or go to sleep...
	
# Extra challenge, do it with one line and use sum() 
def largest_sum(lst1, lst2):
	if sum(lst1) >= sum(lst2): 
		return lst1
	else: 
		return lst2
		
# Well was not one line, maybe you can condense it more -- but sum() sure was handy. Skipped the whole loop. 
	
	
	#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
print(largest_sum([1, 9, 5], [2, 3, 7]))
