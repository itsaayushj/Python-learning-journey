# password intake
# password must be 8 digit or more
# password must contain a symbol 
# password must contain uppercase and lower case
# password must contain numbers


password = input("Enter your password : ")
while True :
    if len(password) < 8 :
        print("Password is too short !")
        password = input("Enter your password : ")
    elif password.islower() or password.isupper() :
        print("Password must contain both uppercase and lowercase!")
        password = input("Enter your password : ")
    elif password.isalpha() or password.isnumeric() :
        print("Password must contain both letter and numbers ") 
        password = input("Enter your password : ")
    elif password.isalnum() :
        print("Password must contain symbols!")
        password = input("Enter your password : ")
    elif " " in password or "\t" in password :
        print("Password must not contain any space!")
        password = input("Enter your password : ")
    else : 
        break

print("Password saved")


