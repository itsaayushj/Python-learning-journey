import random 
import string

character_range = " " + string.ascii_letters + string.digits + string.punctuation 
character_range = list(character_range)
cypher_keys = character_range.copy()
random.shuffle(cypher_keys)

# encryption 

user_input = input("Enter your message : ")
output_text = ""
for letter in user_input : 
    index = character_range.index(letter)
    output_text += cypher_keys[index]

print(output_text)
# decryption 

user_input = input("Enter your message : ")
output_text = ""
for letter in user_input : 
    index = cypher_keys.index(letter)
    output_text += character_range[index]

print(output_text)
    

