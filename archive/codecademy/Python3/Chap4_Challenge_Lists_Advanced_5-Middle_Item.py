# Lists Challenge (Advanced)
# Challenge 20
# Middle Item

# For the final code challenge, we are going to create a function that finds the middle item from a
# list of values. This will be different depending on whether there are an odd or even number values. In the
# case of an odd number of elements, we want this function to return the exact middle value. If there is an even
# number of elements, it returns the average of the middle two elements. Here is what we need to do:

# 1. Define the function to accept one parameter for our list of numbers
# 2. Determine if the length of the list is even or odd
# 3. If the length is even, then return the average of the middle two numbers
# 4. If the length is odd, then return the middle number

# Ok here I think i have to use modulo % to check if it will return 0 (odd or even). But how do I extract the 
# middle without knowing homw many items in the list? Slicing is out the window, or? Google: lol ofc just divide 
# lst by 2. 

# Had to google a bit. This code returned half of whats expected, so I assume it's on 
#def middle_element(lst):
#	if len(lst) % 2 == 0:
#		first = int(len(lst) / 2) - 1 # Googled, -1 
#		last = int(len(lst) / 2)
#		even = first + last / 2
#		return even
#	else: 
#		return int(len(lst)) / 2
		
# Ok so these advanced challenges was hard! I guess somewhat close on the above, but no cigar. 

def middle_element(lst):
	if len(lst) % 2 == 0:
		sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
		return sum / 2
	else:
		return lst[int(len(lst)/2)] # will return 2.5 which then is the middle right?
	
	
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 2, -4, 4, 5]))

