# roulette game
# shoot yourself to keep the gun 


import random 
import time 
score = 0 

ammo = []
current_user = None
# selecting ammo size 
ammo_bullets = int(input("Enter the amount of bullet you want in the ammo : "))
ammo_blanks = int(input("Enter the amount of blanks in the ammo you want :"))
for bullet in range(ammo_bullets) : 
    ammo.append(1)
for blanks in range(ammo_blanks) : 
    ammo.append(0)

print(f"So the ammo is - {ammo}")
total_chamber = len(ammo)
# toss 
while True :
    toss_options = ("heads" , "tails")
    user_toss = input("Choose heads or tails : ").strip().lower()
    while user_toss not in toss_options : 
        print("Invalid")
        user_toss = input("Choose heads or tails : ")
    computer_toss = random.choice(toss_options)
    if user_toss == computer_toss : 
        print(f"User won {user_toss} it was ! You go first")
        current_user = "user"
    else : 
        print(f"You lost {computer_toss} it was ! COmputer go first!  ")
        current_user = "computer"
    Game_on = True
    random.shuffle(ammo)
    current_chamber = 0 
    while Game_on :
        # safety test idk why 
        
        if current_chamber >= total_chamber : # for [0 0 0 0 0 1] length will be 6 but current_chamber can only go upto 5 as index starts from 0 
            print("something went wrong!")
            quit()
       # actual game maybe 
        if current_user == "user" : 
            user_choice = input("press x to shoot yourself and y to shoot the computer").strip().lower()
            if user_choice != "x" and user_choice != "y" : 
                print("invalid")
            elif user_choice == "x" : 
                if ammo[current_chamber] == 0 :
                    print("You shoot yourself! That was a blank")
                    current_chamber += 1
                    remaining_chamber = total_chamber - current_chamber
                    print(f"Chamber status (bullets/chambers remaining) : {ammo.count(1)} /  {remaining_chamber}") 
                    current_user = "user"
                else : 
                    print("You shot yourself ")
                    print("Game over! you lost! ")
                    score -= 1
                    current_user = None
            elif user_choice == "y" : 
                if ammo[current_chamber] == 0 :
                    print("You shoot yourself! That was a blank")
                    print("Gun passes on to the computer")
                    current_chamber += 1
                    remaining_chamber = total_chamber - current_chamber
                    print(f"Chamber status (bullets/chambers remaining) : {ammo.count(1)} /  {remaining_chamber}") 
                    current_user = "computer"  
                else : 
                    print("You shot them! You won ! ")
                    score += 1 
                    current_user = None 
        elif current_user == "computer" : 
            time.sleep(1) # to slow down computers move so user can process it
            #here is a bug remianing chamber
            remaining_chamber = total_chamber - current_chamber
            probablity = ammo.count(1) / remaining_chamber * 100 
            if 0 <= probablity <= 20 :
                computer_chances = ["x" , "x" , "x" , "y"]
            elif 21 <= probablity <= 35 :
                computer_chances = ["x" , "x" , "y"]
            elif 36 <= probablity <= 50 : 
                computer_chances = ["y" , "y" , "x"]
            elif 51 <= probablity <= 70 : 
                computer_chances = ["y" , "y" , "y" , "y" , "x"]
            else : 
                computer_chances = ["y"]
            computer_choice = random.choice(computer_chances)
            if computer_choice == "x" : 
                if ammo[current_chamber] == 0 :
                    print("computer shoot itself! That was a blank")
                    current_chamber += 1
                    remaining_chamber = total_chamber - current_chamber
                    print(f"Chamber status (bullets/chambers remaining) : {ammo.count(1)} /  {remaining_chamber}") 
                    current_user = "computer"
                else : 
                    print("computer shot itself ")
                    print("Game over! you won! ")
                    score += 1
                    current_user = None
            elif computer_choice == "y" : 
                if ammo[current_chamber] == 0 :
                    print("computer shoot user! That was a blank")
                    print("Gun passes on to the user")
                    current_chamber += 1
                    remaining_chamber = total_chamber - current_chamber
                    print(f"Chamber status (bullets/chambers remaining) : {ammo.count(1)} /  {remaining_chamber}") 
                    current_user = "user" 
                else : 
                    print("computer shot you! You lost ! ")
                    score -= 1 
                    current_user = None 
        elif current_user is None : 
            print("--------------------")
            print(f"Your score is  {score}")
            print("--------------------")
            print("Do you wanna play more? ")
            on_or_not = input("Press Y to play more N to quit : ").strip().lower()
            if on_or_not != "y" and on_or_not != "n" :
                print("Invalid")
            elif on_or_not == "y" :
                Game_on = False 
                # hopefully turning it off will not stop it and go  back to main loop as it will be turned back on on main loop 
            else : 
                quit()



