import random
import string
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

# encryption 
user_input = input("Enter your text to encrypt : ")
output_text = ""

for letter in user_input : 
    letter_index = chars.index(letter)
    output_text += keys[letter_index]

print(output_text)

# decryption 

user_input = input("ENter your text to decrypt : ")
output_text = ""

for letter in user_input :
    letter_index = keys.index(letter)
    output_text += chars[letter_index]

print(output_text)

