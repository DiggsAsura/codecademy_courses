# Chap 10
# 1. Learn Python: Files
# 8. Reading a CSV File
#
# Reading a CSV File
# 
# Recall our CSV file from our last exercise: 
# users.csv
#
# <output>
# 
# Even though we can read these lines as text without problems, there are ways to 
# access the data in a format better suited for programming purposes. In Python
# we can convert that data into a dictionary using the csv library's DictReader 
# object. Here's how we'd create a list of the email adresses of all of the users
# in the aove table: 
#### OK THIS IS GOOD STUFF. Something I can start apply pretty quitck into something
#### useful :D 
#
import csv
#
list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
	user_reader = csv.DictReader(users_csv)
	for row in user_reader:
		list_of_email_addresses.append(row['Email'])

print(list_of_email_addresses)
# This example i can try with own customer list. Just not upload that to github haha. 
#
# In the above code we first imported our csv library, which gives us the tools to
# parse our CSV file. We then create the empty list list_of_email_addresses which
# we'll later populate with the email addresses from our CSV. Then we open
# the users.csv file with the temporary variable users_csv.
#
# We pass the additional keyword argument newline='' to the opening open() function
# so that we don't accidentally mistake a line break in one of our data fields as a 
# new row in our CSV (read more about this in the Python documentation). 
#
# After opening our new CSV file we use csv.DictReader(users_csv) which converts
# the lines of our CSV file to Python dictionaries which we can use to access 
# methods for . The keys of the dictionary are, by default, the entries in the 
# first line of our CSV file. Since our CSV's first line calls the third field in 
# our CSV "Email", we can use that as the key in each row of our DictReader.
#
# When iterate through the rows of our user_reader object, we access all of the
# rows in our CSV as dictionaries (except for the first row, which we used to 
# label the keys of our dictionary). By accessing the 'Email' key of each of these
# rows we can grab the email address in that row and append it to our
# list_of_email_addresses.

# Tasks
# 1. Import the csv module
#
# 2. Open up the file cool_csv.csv in the temporary variable cool_csv_file
#
# 3. Using csv.DictReader read the contents of cool_csv_file into a new
# 	 variable called cool_csv_dict
#
# 4. cool_csv.csv included a cool fact about every person in the CSV. 
# 
#		 For each row in cool_csv_dict print out that row's "Cool Fact".

import csv

with open('cool_csv.csv') as cool_csv_file:
	cool_csv_dict = csv.DictReader(cool_csv_file)
	for row in cool_csv_dict:
		print(row["Cool Fact"])

