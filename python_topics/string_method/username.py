# username should not more than 12 character
# must not contain spaces 
# must not contain digits
username = input("Enter your username :")
#user_count = len(username)
#print("Username too long" if len(username) > 12 else "Username is in limited characters ✅")
#print("NO Space or digits is allowed" if username.isalpha() == False else "Username is okay" )
if len(username) > 12 or username.isalnum() or username.isspace() :
#if len(username) > 12 or username.isalpha() == False :
    print("Username is invalid")
else :
    print("username is valid")

# alternative method : (as in tutorial)

#if username.count(" ") == -1 : #-1 means no blanks 
 #   print(" blanks are not allowed in username")