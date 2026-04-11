import random 
core = ("rock" , "paper" , "scissors")
score = 0
is_running = True
while is_running :
    computer = [ random.choice(core), random.choice(core)]
    # computer.append(random.choice(core))
    # computer.append(random.choice(core))
    user = []

    while True :
        user_hand1 = input("Enter your first hand : ").strip().lower()
        if user_hand1 not in core : 
            print("Invalid choice")
            continue
        user_hand2 = input("Enter your second hand : ").strip().lower()
        if user_hand2 not in core : 
            print("Invalid choice")
            continue
        break
    user = [user_hand1 , user_hand2]
    print("Your hand - " , end = " ")
    for hand in user : 
        print(hand , end=" ")
    print("")
    print("computer's hand - " , end = " ")
    for hand in computer : 
        print(hand , end=" ")
    print("")
    user_final = input("Enter your final hand from selected hands: ")
    while user_final not in user : 
        print("Invalid choice")
        user_final = input("Enter your final hand from selected hands: ")
    computer_new = random.choice(computer)
    if computer >10 :
        while True : 
            if (computer_new == "rock" and user == "scissors") or (computer_new == "paper" and user == "rock") or (computer_new == "scissors" and user == "paper"):
                    print("You Lost!!!")
                    print(f"{computer_new} beats {user}")
                    score -= 1
                    print(f"Your score is - {score}")
                    break
            elif computer_new == user :
                    print("ITS A DRAW!")
                    print(f"Your score is - {score}")
                    break
            else : 
                    print("YOU WON")
                    print(f"{user} beats {computer_new}")
                    score += 1
                    print(f"Your score is - {score}")
                    break
            start_or_stop = int(input("press 1 to play one more time / 0 ot stop"))
            if start_or_stop == 0  : 
                is_running = False
            else : 
                continue 



