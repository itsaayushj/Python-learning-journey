password = input("Enter your password :  ")
while True : 
    if len(password) < 12 :
        print("Username too small !")
        password = input("Enter your password : ")
    elif password.isupper() == True or password.islower() == True : 
        print("Password must contain both uppercase and lowercase letters !")
        password = input("Enter your password : ")
    elif password.count(" ") != 0 or password.count("\t") != 0 :
        print("password must not contain space ")
        password = input("Enter your password : ")
    elif password.isalnum() == True :
        print("Passoword must Contain signs : ")
        password = input("Enter your password : ")
    else :
        break 

print("Password saved")
