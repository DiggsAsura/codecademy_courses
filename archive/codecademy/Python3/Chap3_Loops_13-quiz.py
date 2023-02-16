
# I STILL CAN'T UNDERSTAND THE MODULO OPERATOR! GDI
# sooomewhat got this now. but not quite. modulo operator asks the remaider, and this 
# example 2 divided by 2 will be 0, then it will skip 2. in my head it would print only 2, but 
# for some reason it's the opposite, where it print all but 2. 
numbers = [1, 1, 2, 3]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

# WHY THE HELL DOES IT PRINT 4 TIMES? WHERE DOES IT GET 4 FROM??
# oki breath, because it's not connected to the actual numbers, it's connected to the amount of items in the list
numbers = [2, 4, 6, 8]
for number in numbers:
    print("hello!")

# Failed on this for some reason, even though I done similar quite a few times during 
# the course. Writing down here to try help memorise better
grouped_topics = [["Alorithms", "Data Science", "AI"], ["Linear Regression", "SQL"]]

for sublist in grouped_topics:
    for sublist_element in sublist:
        print(sublist_element)