# # weather checker
# temp = float(input("Temperature in celcius"))
# sunornot = input("Is there sun outside or is it cloudy ?")
# if temp >= 30 and sunornot == "cloudy" :
#      print("dont step foot outside sir")
# else :
#      print("pass")

# sun =False
# temp = 35
# if temp > 30 and not sun :
#     print("Hot and cloudy ") 
# else :
#     print("pass")



# conditional statment
# sun =True
# temp = 35
# print("cloudy but hot" if temp > 30 and not sun else "Pass it")

# print("facts" if 2+2==5 else "all lies")
#even or odd
# number = 21
# print("Even" if number % 2 == 0 else "Odd")

#couter
import random
magic_number = random.randint(1,100)
guess = input("Enter your guess :")
while True :
    if guess.isnumeric() == False :
        print("Guess was not a valid number!")
        guess = input("Enter your guess :")
    else :
        guess = int(guess)
        if guess > 100 or guess < 0 :
            print("Number out of range !")
            guess = input("Enter your guess :")
        else :
    

            while True :
                diff = magic_number - guess 
                if diff >= 20 :
                    print("Guess was too big !")
                elif diff >= 10 :
                    print("Guess was Big!")
                elif diff <= 20 :
                    print("Guess was too small !")
                elif diff <= 10 :
                    print("Guess was small !")
                else :
                    print("guess was correct!")

                guess = input("Enter your guess :")









