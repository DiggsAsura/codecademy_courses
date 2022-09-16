# Chapter 6 - Python Code Challenges
# Functions (Advanced) - 4
# Dog Years

# Let's create a function which calculates a dog's age in dog years! This function will accept the name of the dog
# and the age in human years. It will calculate the age of the dog in dog years and return a string describing
# the dog's age. This will require a few steps. 

# 1. Define the function called dog_years to accept two parameters: name and age
# 2. Calculate the age of the dog in dog years
# 3. Concatenate the string with the dog's name and age in dog years
# 4. Return the resulting string

# Quirky and a bit funny lesson I guess. Think I got this. Might have to include str() and/or int() as I'm not
# really rock solid on when these are used and needed. 

def dog_years(name, age): 
	#return name + ", you are " + (age * 7) + " " + " years old in dog years"
	# Yeaaa, as suspected and mentioned above. Need to convert it to strint to concatenate I guess
	return name + ", you are " + str(age * 7) + " years old in dog years"
	
# Ok beside the first conversion to str() I got it. 

print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"
