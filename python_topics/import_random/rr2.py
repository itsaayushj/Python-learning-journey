# roulette game
# 1 bullet , 6 chambers 
# shoot yourself to krrp gun or shoot the opps to pass it to opps 
import random 
import time

current_player = None
total_score =  0
game_on = True
while game_on :
#toss 
    toss_options = ("heads" , "tails")

    user_toss = input("Enter heads or tails : ").lower().strip()

    while user_toss not in toss_options : 
        print("Invalid ")
        user_toss = input("Enter heads or tails : ").lower().strip()
    computer_toss = random.choice(toss_options)

    if user_toss == computer_toss : 
        print(f"It's {computer_toss}.You won ! ")
        current_player = "user"

    else : 
        print(f"It's {computer_toss}.You lost !")
        current_player = "computer"

    #game 
    mag = [ 0 , 0 , 0 , 0 , 0 , 1]
    current_chamber = 0
    random.shuffle(mag)
    while current_player is not None :
        if current_chamber >= 6 : 
            break  
        remaining_chamber = len(mag) - current_chamber
        probablity = 1 / remaining_chamber * 100 
        if current_player == "user" : 
            user_shot_choice = input("press x to shoot yourself, y to shoot the opps!").lower().strip()
            while user_shot_choice != "y" and user_shot_choice != "x" : 
                print("invalid choice!")
                user_shot_choice = input("press x to shoot yourself, y to shoot the opps!").lower().strip()
            if user_shot_choice == "x" : 
                if mag[current_chamber] == 0 :
                    print("that was a blank !")
                    current_chamber += 1 
                    print(f"1 / {remaining_chamber} is remaining")
                    current_player = "user"
                else : 
                    print("You shot yourself !")
                    current_player = None
                    total_score -= 1
                    # break
            elif user_shot_choice == "y" : 
                if mag[current_chamber] == 0 : 
                    print("That was a blank")
                    current_chamber += 1 
                    print(f"1 / {remaining_chamber} is remaining")
                    current_player = "computer"
                    
                else : 
                    print("YOU SHOT THEM ! You won ")
                    current_player = None 
                    total_score += 1 
                    # break 
        elif current_player == "computer" :
                if probablity <= 25 : 
                    choice_probablity = ["x" , "x" , "y"]
                elif 25 < probablity < 50 : 
                    choice_probablity = ["x" , "y"] 
                else : 
                    choice_probablity = ["x" , "y" , "y" , "y"]
                computer_decision = random.choice(choice_probablity)
                if computer_decision == "x" : 
                    if mag[current_chamber] == 0 :
                        print("Compuet is making a choice....")
                        time.sleep(1)
                        print("computer choose to shoot itself")
                        print("that was a blank !")
                        current_chamber += 1 
                        print(f"1 / {remaining_chamber} is remaining")
                        current_player = "computer"
                    else : 
                        print("Compuet is making a choice....")
                        time.sleep(1)
                        print("computer shot itself !")
                        current_player = None
                        total_score += 1 
                        # break
                elif computer_decision == "y" :  
                    if mag[current_chamber] == 0 :
                        print("Compuet is making a choice....")
                        time.sleep(1) 
                        print(" computer choose to shoot you !That was a blank")
                        current_chamber += 1 
                        print(f"1 / {remaining_chamber} is remaining")
                        current_player = "user"
                    else : 
                        print("Compuet is making a choice....")
                        time.sleep(1)
                        print("computer shot you ! You lost ")
                        current_player = None 
                        total_score -= 1
                        # break 
    if current_player is None : 
        print("------------------------------------")
        print(" Game Over !")
        print(f"Your score is {total_score}")
        print("Do YOU WANNA PLAY AGAIN ?")
        print("------------------------------------")
        on_or_off = input("press y to play again and n to stop").strip().lower()
        while on_or_off != "y" and on_or_off != "n" : 
            print("invalid")
            on_or_off = input("press y to play again and n to stop").strip().lower() 
        if on_or_off == "y" : 
            continue 
        else : 
            game_on = False