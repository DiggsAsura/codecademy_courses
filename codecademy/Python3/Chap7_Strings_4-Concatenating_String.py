# Chap 7 - Strings
# 4. Concatenating Strings

# Touching on concatenating again. Intro reminds us about theres no space, so if you want to concatenate 
# with spaces, you have to add that either in " ", or added space at the end of a string


first_name = "Julie"
last_name = "Blevins"


# 1. Write a function called account_generator() that takes two inputs, first_name and last_name and 
#    concatenates the first three letters of each and return the new account name
# 2. Test your function on the first_name and last_name provided and save it to a variable new_account

def account_generator(first_name, last_name):
	return (first_name[0:3] + last_name[0:3])
	
new_account = account_generator(first_name, last_name)
print(new_account)
