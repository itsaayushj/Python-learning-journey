# encryption - decryption 
import random 
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation 

chars = list(chars)

keys = chars.copy()
random.shuffle(keys)

output_text = ""
# encode 
input_text = input("Enter your message : ")
for text in input_text : 
    index = chars.index(text)
    output_text += keys[index]

print(output_text)

# decode 
output_text = ""
input_text = input("Enter your message : ")
for text in input_text : 
    index = keys.index(text)
    output_text += chars[index]
print(output_text)
