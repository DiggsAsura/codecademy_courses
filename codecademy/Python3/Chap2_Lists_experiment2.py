my_list = ["0. Music", "1. Linux", "2. Video Games"]
print(my_list)

print("Which item do you want to delete?")
delete_item = my_list.pop(int(input()))

print(my_list)

print("Are you sure you want to delete", delete_item + "?")

answer = input("y/n: ")

if answer == "y":
    print(delete_item, "deleted...")
        # At this point I can't seem to figure how to actually delete the pop'ed item...
        # or actually know if it's needed at all. Following code this not work.  
        #deleted_item = int(delete_item)
        #deleted_item.remove(0)
    print(my_list)
elif answer == "n":
    print(delete_item, "is moved back to your list!")
    my_list.insert(-1, delete_item)
    print(my_list)
else:
    # Don't know at this point how to get this to loop if no valid answer is given
    print("Please choose y or n, try again: ")


