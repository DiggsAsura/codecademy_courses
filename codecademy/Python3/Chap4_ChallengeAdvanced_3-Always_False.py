# Control Flow (Advanced)
# Challenge 8
# Always False

# There are some situations that you normally want to avoid when programming using conditional statements. One
# example is a contradiction .This occurs when your condition will always be false no matter what value you
# pass into it. Let's create an example of a function that contains a contradiction. It will contain a few steps: 

# 1. Define the function to accept a single parameter called num
# 2. Use a combination of <, > and "and" to create a contradiction in an if statement
# 3. If the condition is true, return True, otherwise return False. The trick here is that because we've
# written a contradiction, the condition should never be true, so we should expect to always return False.

# ok this one is actually a bit challanging! It probably should not be, but rn I can't really provoke it! The 
# intention of this is to LEARN how NOT to do, as this is something you very rarly wanna do in programming.

def always_false(num):
	if num < -2 and num > 2:
		return True
	return False
	
# Ok, it was not hard really lol. Overthought it a bit? To sleepy? Just had to think for a min and it was easy 
# peasy. Again, the solution after also wants the if statement in ()'s but is it really so? Perfectly fine without..
# They also suggest else: but it was not needed either. Anyhow, got it :) 
# Oh and they went with 0 and 0 - probably more in line with their intention. 
	
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

