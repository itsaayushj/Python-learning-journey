user_password = input("Enter your password : ")
while len(user_password) < 8  or " " in user_password : 
    print("Invalid password !")
    user_password = input("Enter your password : ")

has_uppercase = False
has_lowercase = False 
has_numbers = False 
has_symbols = False
score = 0
for i in user_password : 
    if i.isupper() : 
        has_uppercase = True 

    elif i.islower() :
        has_lowercase = True 

    elif i.isnumeric() : 
        has_numbers = True 

    elif not i.isalnum() : 
        has_symbols = True 

if has_lowercase : 
    score += 1 
if has_numbers : 
    score += 1 
if has_symbols : 
    score += 1 
if has_uppercase : 
    score += 1

if score <= 1 : 
    print("Not tuff lil bro ")
elif 1 < score < 3 : 
    print("Mid af ngl ")
else : 
    print("Nah homie you tuff ")

    