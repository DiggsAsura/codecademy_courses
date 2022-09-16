# Control Flow (advanced)
# Challenge 6 - In Range

# Let's start the advanced challenge problems by testing if a number falls within a certain range. We will
# accept three parameters where the first parameter is the number we are testing, the second parameter is the 
# lower bound and the third parameter is the upper bound of the range. These are the steps required:

# 1. Define the function to accept three numbers as parameters
# 2. Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound
# 3. If this is true, return True, otherwise return False

# Hmm is this nesting or elif? Hunch on nesting, trying that first
# Actually, gonna pivot and use "and". Might be wrong

def in_range(num, lower, upper):
	if num >= lower and num <= upper:
		return True
	else:
		return False
		
# ok nice, the pivot was good thinking :) That was correct
# however, note to self - did not need to use else: return False! Could just do like this:

#def in_range(num, lower, upper):
#  if(num >= lower and num <= upper):
#    return True
#  return False

# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
