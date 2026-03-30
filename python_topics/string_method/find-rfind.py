# length of the name 
name = input("Please enter your full name :")
length = len(name)
print(f"Length of your name was {length}")

first_occurance = name.find("a")  # to find when the first time A occured in name
# it starts it count from 0 
# to find the last time when A occured we use reverse find or rfind
last_occurance = name.rfind("a") # if i write a insted of A it will return -1 as in it never occured

print(first_occurance , last_occurance)

name = name.capitalize() #capitalsie the first letter of name
name = name.upper() # uppercase every letter
name = name.count("a")
name = name.lower() # lowercase every letter
#name = name.isdigit() #to check if all string is number only
name = name.isalpha()  #it does not work with bools...... at above i used .isdigit() and so .isalpha did not work because it was a boolean and no more a string 
print(name)

print(help(str))