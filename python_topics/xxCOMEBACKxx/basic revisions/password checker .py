password = input("Enter your password : ")
while len(password) < 8 :
    print("Password too short")
    password = input("Enter the password : ")
else :
    while password.isalpha() != False or password.isdigit() != False :
        print("Password must contain both number and letters")
        password = input("Enter the password : ")
    else : 
        while password.isalnum() == False :
            print("Password Must not contain symbols or space")
            password = input("Enter the password : ")
        else : 
            while password.islower() == True or password.isupper() == True :
                print("Password Must contain both uppercase and lowercase")
                password = input("Enter the password : ")

print("Password saved !")
