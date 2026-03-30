import random
core = ( "rock" , "paper" , "scissors")
is_running = True
start_or_stop = None
score = 0 
while is_running : 
    computer = random.choice(core)
    user = input("Enter your choice : ").lower().strip()
    if user  not in core :
        print("Invalid choice!")
        user = input("Enter your choice : ").lower().strip()
    else :
        print(computer)
        if (computer == "rock" and user == "scissors") or (computer == "paper" and user == "rock") or (computer == "scissors" and user == "paper"):
            print("You Lost!!!")
            print(f"{computer} beats {user}")
            score -= 1
            print(f"Your score is - {score}")
        elif computer == user :
            print("ITS A DRAW!")
            print(f"Your score is - {score}")
        else : 
            print("YOU WON")
            print(f"{user} beats {computer}")
            score += 1
            print(f"Your score is - {score}")
    start_or_stop = int(input("press 1 to play one more time / 0 ot stop"))
    if start_or_stop == 0  : 
        is_running = False
    else : 
        continue 
