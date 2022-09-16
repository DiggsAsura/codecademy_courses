# Control Flow (Advanced)
# Challenge 10
# Max Number

# For the final challenge, we are going to select which number from three input values is the greatest using
# conditional statements. To do this, we need to check the different combinations of values to see which number
# is greater than the other two. Here is what we need to do:

# 1. Define a function that has three input parameters, num1, num2, num3
# 2. Test if num1 is greater than the other two numbers:
#       3. If so, return num 1
# 4. Test if num2 is greater than the other two numbers:
#				5. If so, return num2
# 6. Test if num3 is greater than the other two numbers:
#       7. If so, return num3
# 8. If there was a tie between the two largest numbers, then return "It's a tie!"

# Ok, sounds easy enough. Slightly mindbugged by point 8, but lets start going with the function. Might just be else

def max_num(num1, num2, num3):
	if num1 > num2 and num1 > num3:
		return num1
	elif num2 > num1 and num2 > num3:
		return num2
	elif num3 > num1 and num3 > num2:
		return num3
	else: 
		return "It's a tie!"
		
# Ok I think it's easy as this really. 
# Aaand boom it was. Nice and easy :D

# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

