# Write your tip function here:

# Create a cunction tip() with parameter total and percentage. Should retrun the amount you should tip given a total and the percentage you want to tip.

def tip(total, percentage):
  # first fail. basically, i need to go over my basic math! haha
  #return total + (total * percentage)
  return (total * percentage) / 100
  
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
