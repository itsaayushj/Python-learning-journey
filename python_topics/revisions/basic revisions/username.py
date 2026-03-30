# max 12 character
# no number
# no spaces 
username = input("Enter your username : ")
while True :
    if len(username) > 12 :
        print("Username too long")
        username = input("Enter your username : ")
    elif username.isalpha() == False :
        print("Username must not contain numbers and space ")
        username = input("Enter your username : ")
    else :
        break

print("Username registered.")