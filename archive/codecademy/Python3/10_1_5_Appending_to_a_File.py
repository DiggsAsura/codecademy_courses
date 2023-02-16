# Chap 10
# 1. Learn Python: Files
# 5. Appending to a File

# Appending to a File
#
# So maybe completly deleting and overwriteing existing files is something
# that bothers you. Isn't there a way to just add a line to a file without
# completly deleting it? Of course there is! Instead of opening the file 
# using the argument 'w' for write-mode, we open it with 'a' for append-mode. 
# If we have a generated file with the following contents
#
# generated_file.txt
# This was a popular file...
#
# Then we can add another lin to that file with the following code:
#
# with open('generated_file.txt', 'a') as gen_file:
# 	gen_file.write("... and it still is")
# 
# In the code above we open a file object in the temporary vaiable gen_file.
# This vaiable points to the file generated_file.txt and, since it's open in append-
# mode, add the line ... and it still is as a new line to the file. If you were to 
# to open the file after running the script it would look like this:
#
# This was a popular file...
# ... and it still is
#
# Notice that opening the file in append-mode, with 'a' as an argument to open(), 
# means that using the file objet's .write() method appends whatever is passed to 
# the end of the file in a new line. If we were to run the script.py again, this
# would be what generated_file.txt would look like:
#
# This was a popular file...
# ... and it still is
# ... and it still is
#
# Notice that we've appended "... and it still is" to the file a second time! This 
# is because in script.py we opened generated_file.txt in append mode.

# Tasks
# 1. We've got a file, cool_dogs.txt, filled with all the cool dogs we know. 
#  	 Somehow while compiling the list we forgot about one very cool dog. Let's fix
#    that problem by adding him to our cool_dogs.txt
#
#		 Open up our file cool_dogs.txt in append-mode and assign it to the file
#    object cool_dogs_file
#
# 2. Inside your with block, add "Air Buddy" to cool_dogs.txt. Air Buddy is a 
#    Golden Retriever that plays basketball, which more than qualifies him 
# 	 for this list. 


with open('cool_dogs.txt', 'a') as cool_dogs_doc:
	cool_dogs_doc.write("Air Buddy")

