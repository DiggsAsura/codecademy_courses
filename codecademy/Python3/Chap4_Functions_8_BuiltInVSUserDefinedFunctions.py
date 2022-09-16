tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:

# We been using built-in functions() all along! print() str() int()

# Even a function for help!
# help("String")


# use Python doc to read up on max()
# max() returns the 

# Failed but not failed. I mide a two dimensional list when the Task really only ask for the value
#max_price = max(["T-shirt:", 9.75], ["Shorts:", 15.50], ["Mug:", 5.99], ["Poster:", 2.00])

max_price = max(9.75, 15.50, 5.99, 2.00)
min_price = min(9.75, 15.50, 5.99, 2.00)
# i get the right output on round(), but fails the task hmm
tshirt_price = 9.75
# ok the error was i didnt read one detail, aka just 1 to round up the decimal only
rounded_price = round(tshirt_price, 1)

print(max_price)
print(min_price)
print(rounded_price)
