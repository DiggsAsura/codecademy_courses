# Control Flow (Advanced)
# Challenge 7
# Same Name

# We need to write a program that checks different names and determines if they are equal. We need to 
# accpet two strings and compare them. Here are the steps:

# 1. Define the function to accept two strings, your_name and my_name
# 2. Test if the two strings are equal
# 3. Return True if they are equal, otherwise return False

# can it be this simple? again, a bit unsure if = or == but gonna try run with single = first
# also, gonna try to see if return false without else gonna do it

def same_name(your_name, my_name):
	if your_name == my_name:
		return True
	return False
	
# nope, not that easy. Getting syntax error on =, use ==
# ok, got it. this was as easy as.... lowercase true and false. Remember capital T and F! Just edited the code. 
# AND == for comparing strings! Idk if its strings only, I feel i seen like this == 0, but yea..  
# The hint afterwards suggest if (your_name == my_name) inside () however it ran just fine without. 
# The hint also suggested else: return False, however, looks like, for this example, just return False 
# also did it. 


# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False
