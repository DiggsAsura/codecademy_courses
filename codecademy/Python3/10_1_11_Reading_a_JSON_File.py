# Chap 10
# 1. Learn Python: Files
# 11. Reading a JSON File

# Reading a JSON File
# 
# CSV isn't the only format the Python has built-in library for. We can also use
# Python's file tools to read and write JSON. JSON, an abbreviation of 
# JavaScript Object Notation, is a file format inspired by the programming language
# JavaScript. The name, like CSV is a bit of a misnormer - some JSON is not 
# valid JavaScript (and plenty of JavaScript is not valid JSON).
#
# JSON's format is endearingly similar to Python dictionary syntax, and so JSON files
# might be easy to read from a Python developers standpoint. Nonetheless, Python
# will help us parse JSON files into actual Python dictionaries. Suppose we have a 
# JSON file like the following:
#
# purchase_14781239.json
#
#{
#  'user': 'ellen_greg',
#  'action': 'purchase',
#  'item_id': '14781239',
#}
#
# We would be able to read that in as a Python dictionary with the following code:
#
#import json
# 
#with open('purchase_14781239.json') as purchase_json:
#  purchase_data = json.load(purchase_json)
# 
#print(purchase_data['user'])
#
# First we import the json package. We opened the file using our trusty open() 
# command. Since we're opening it in read-mode we just need to pass the file name.
# We save the file in the temporary variable purchase_json.
#
# We continue by parsing purchase_json using json.load(), creating a Python 
# dictionary out of the file. Saving the results into purchase_data means we
# can interact with it. We print out one of the values of the JSON file by 
# keying into the purchase_data object.

# Taks
# 1. Let's read a JSON file! Start by importing the json module.
#
# 2. Open up the file message.json, saving the file object to the
# 	 variable message_json.
#
# 	 Open the file in read-mode, without passing any additional arguments to open()
#
# 3. Pass the JSON file objects as an argument to json.load() and save the 
# 	 resulting Python dictionary as message
#
# 4. Print out message['text']

import json

with open('message.json') as message_json:
	message = json.load(message_json)

print(message['text'])
