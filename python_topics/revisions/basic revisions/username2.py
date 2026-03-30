# username set
#12 letter max
# 8 letter min 
# no space 
# uppercase with symbols

username = input("Enter your username : ")
while True:
    if not  8 <= len(username) <= 12 :
        print("Username must be between 8 to 12 characters")
    elif username.count(" ") != 0  or username.count("\t") != 0:
        print("Username must not contain any space")
    elif username.isupper() or username.islower() :
        print("Username must contain both uppercase and lowercase letters")
    elif username.isalnum() :
        print("username must contain symbols")
    else :
        break 
    
    username = input("Enter your username : ")

print("username registered!")
