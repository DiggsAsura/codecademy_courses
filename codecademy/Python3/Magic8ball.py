# Task 1
name = input("Your name: ")
name = str(name)
# Task 2
question = input("Your question: ")
question = str(question)
# Task 3
answer = ""
# Task 4
import random
# Task 5
random_number = random.randint(1, 11)
#random_number = 10
#print(random_number)

# Task 6, 7 and 8
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
#Task 12
elif random_number == 10:
  answer = "Kenny says yo"
elif random_number == 11:
  answer = "Jing says no"
else:
  answer = "Error"


# Task 9, 10, 11, 13
#if name == "" or len(name) == 0:
#  print(question)
#else:
#  print(name, "asks:", question)
#print("Magic 8-Ball's answer:", answer)

# Task 14
#if question == "" or len(question) == 0:
#  print("There is no question.")
#else:
#  print(name + " asks: " + question)
#  print("Magic 8-Ball's answer: " + answer) 


# My own take
# No Name, No Question
if len(name) == 0 and len(question) == 0:
  print("There is no name nor a question")
# No Name, Question
elif len(name) == 0 and len(question) > 0:
  print("Magic 8-Ball's answer:", answer)
# Name, No question
elif len(name) >= 1 and len(question) == 0:
  print("Hey", name + "! You forgot to add the question!")
#Name, Question
else: 
  print(name, "asks: ", question)
  print("Magic 8-Ball's answer:", answer)

