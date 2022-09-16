# Chap 7 - Strings
# Cut Me a Slice of String

# OK think we might just go waaay back and we quite speedy go into deeper stuff yea. Fingers crossed :D
# Now we're on slicing. 

# string[first_index:last_index]
# Try to remember:
# This example will include the first_index, up to, but exclude last_index

# start from beginning, up to but exclude [:5]
# start from index all the way until the end [4:]


first_name = "Rodrigo"
last_name = "Villanueva"


# 1. Creat a variable new_account by slicing the first five letters of his last_name
# 2. Create a variable called temp_password by creating a slice out of the third through sixth letters of last_name
#    Your string should have a total of 4 chars. 
new_account = last_name[:5] # remember this is acutllay "6", but skipping the sixth
temp_password = last_name[2:6] 

print("Account name: " + new_account)
print("Temp password: " + temp_password)

