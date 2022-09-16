# Chap 10 - Files
# 1. Learn Python: Files
# 1. Reading a File

# Phew, finally hussled myself through that god aweful jupyter notebook awefulness 
# with that way to complicated offplatform thingy. God dam, Jupyter makes it 
# soooo messy too. Screw that. 

# Reading a File
#
# Computers use file systems to store and retrieve data. Each file is an individual 
# container of related information. If you've ever save a document, downloaded a song, 
# or even sent an e-mail you've created a file on some computer somewhere. Even 
# script.py, the Python program you're editing in the learning enviroment, is a file.
#
# So, how do we interact with files using Python? We're going to learn how to read and 
# write different kinds of files using code. Let's say we had a file called 
# real_cool_document.txt with these contents: 
#
# real_cool_document.txt
# Wowsers!
#
# We could read that file like this:
with open('real_cool_document.txt') as cool_doc:
	cool_contents = cool_doc.read()
print(cool_contents)
#
# This opens a file object called cool_doc and creates a new indented block 
# where you can read the contents of the opened file. We can read the contents 
# of the file cool_doc using cool_doc.read() and save the resulting string into
# the variable cool_contents. Then we print cool_contents, which outputs the 
# statement <content of real_cool_document.txt>

# Tasks
# 1. Use with to open the file welcome.txt. Save the file object as text_file
#
# 2. Read the contents of text_file and save the results in text_data.
#
# 3. Print out text_data.


with open('welcome.txt') as text_file:
	text_data = text_file.read()

print(text_data)
