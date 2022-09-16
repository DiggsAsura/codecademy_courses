message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
alpha = "abcdefghijklmnopqrstuvwxyz"
punct = "!.?,' "
#print(letter)

#def caesar_cipher(string):
#	alpha = ['a', 'b', 'c,', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']
#	new_string = []
#	for i in string:
#		new_string.append(i)
#		if new_string[i] == alpha[i]:
#			print(i)
#	return new_string
  
#print(caesar_cipher(letter))
# Nope. I think I kind of have the right ideas, but we do not work with lists[] here, directly with strings instead. 

translated_message = ""
for letter in message:
	if letter not in punct: # can i write it if letter not in punct?
		letter_value = alpha.find(letter)
		translated_message += alpha[(letter_value + 10) % len(alpha)]
	else:
		translated_message += letter
		
print(translated_message)
		
message_for_v = "Hey man! Cool cipher, thanks for showing me V! You got anything else going on?"
trans_mes = ""
for letter in message_for_v:
	if letter not in punct:
		letter_value = alpha.find(letter)
		trans_mes += alpha[(letter_value - 10) % len(alpha)]
	else:
		trans_mes += letter

print(trans_mes)

# part 1 and 2 of this off platform project. It's big so I separate them.
