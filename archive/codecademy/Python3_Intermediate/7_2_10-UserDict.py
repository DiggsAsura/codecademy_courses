# 7. Specialized Collections
# 2. Collections
# 10. UserDict

print('\nUserDict\n-----------------')

# In this lesson, we have seen advanced containers which modify the functionality
# of a dictionary such as the defaultdict and OrderedDict. The UserDict container
# wrapper lets us create our own version of a dictionary. This class contains all
# of the functionality of a normal dict, except that we can access the 
# dictionary data through the data property. Here's an example of creating
# a modified dictionary:

from collections import UserDict

#? Create a class which inherits from UserDictClass
class DisplayDict(UserDict):
  #? A new method to increase the dictionary's functionality
  def display_info(self):
    print("Number of Keys: " + str(len(self.keys())))
    print("Keys: " + str(list(self.keys())))
    print("Number of Values: " + str(len(self.values())))
    print("Values: " + str(list(self.values())))

  #? We can also overwrite a method from the dictionary class
  def clear(self):
    print("Deleting all items from the dictionary!")
    super().clear()

disp_dict = DisplayDict({'user': 'Mark', 'device': 'desktop', 'num_visits': 37})

disp_dict.display_info()
disp_dict.clear()    
disp_dict.display_info() # 0

# As shwon in this code example, we can add additional methods and overwrite 
# methods from the UserDict class. This is the same as inheriting from regular
# classes in Python.
#
# Now let's create our own dict class!


print('\nTasks\n------------')

# 1. Let's try creating a new dictionary which is able to clear orders which are
#    already processed when the method .clean_orders() is called. 
#    Import the UserDict class and create a new class which inherits from it
#    called OrderProcessingDict. The .clearn_orders() method should search
#    for any keys called 'order_status' and if value is equal to 'complete', 
#    remove the entire oder from the dictionary.
#
# 2. Now that you have created your own class, try creating an instance of it
#    called process_dict while passing data into the constructor. Afterwards,
#    call the .clean_orders() method to automatically clean the orders 
#    inside. You can also print your custom dictionary to see the results. 


data = {
  'order_4829': {
    'type': 't-shirt',
    'size': 'large',
    'price': 9.99,
    'order_status': 'processing'
  },
  'order_6184': {
    'type': 'pants',
    'size': 'medium',
    'price': 14.99,
    'order_status': 'complete'
  },
  'order_2905': {
    'type': 'shoes',
    'size': 12,
    'price': 22.50,
    'order_status': 'complete'
  },
  'order_7378': {
    'type': 'jacket',
    'size': 'large',
    'price': 24.99,
    'order_status': 'processing'
  }
}

from collections import UserDict

class OrderProcessingDict(UserDict):
  def clean_orders(self):
    to_del = []
    for key, value in self.items():
      if value['order_status'] == 'complete':
        print(f'{key}: {value["order_status"]}')
        print('Deleting order....')
        print('Done.')
        to_del.append(key)
    
    for item in to_del:
      del self.data[item]


process_dict = OrderProcessingDict(data)

print('Orders before processing:')
for order in data:
  print(order)

print('')
process_dict.clean_orders()
print('')


print('Orders after cleanup:')
for order in process_dict:
  print(order)