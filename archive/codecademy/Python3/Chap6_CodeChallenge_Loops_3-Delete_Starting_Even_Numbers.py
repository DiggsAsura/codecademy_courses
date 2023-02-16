# Chapter 6 - Python Code Challenges
# Loops 3
# Delete Starting Even Numbers

# Let's try a tricky challenge involving removing elements from a list. This function will repeatedly remove
# the first element of a list until it finds an odd number (break???) or runs out of elements. 
# It will accept a list of numbers as an input parameter and return the modified list where any even numbers at 
# the beginning of the list are removed. To do this, we need the following steps:

# 1. Define our function to accept a single input parameter (lst) which is a list of numbers
# 2. Loop through every number in the list if there are still numbers in the list and if we haven't hit an 
#    odd number yet
# 3. Within the loop, if the first number in the list is even, then remove the first number of the list
# 4. Once we hit an odd number or we run out of numbers, return the modified list

# Okies, we need break if it find a odd number. To distinguish if the number is even or odd, i assume we need 
# to use modulo (modulus?) %. I'm unsure if this maybe a while loop, not for..

#def delete_starting_evens(lst):
#	while len(lst) > 0:
#		for i in lst:
#			if i % 2 == 0:
#				lst = lst[1:]
#	return lst
			
# ok i think above code broke the codecademy interpreter. lol. Just spinning. Great. If that means can not use
# for loop inside a while loop idk. But anyhow it was wrong... 


# and reading the solution, offff it's so easy, i just could not wrap my head around it now. Focus a bit all over
# the place. 
def delete_starting_evens(lst):
	while (len(lst) > 0 and lst[0] % 2 == 0):
		lst = lst[1:]
	return lst
	
	
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
