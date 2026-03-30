print("Lets play rock paper scissors!")
rock = "rock"
paper = "paper"
scissors = "scissors"

opponents_move = input("Enter your move :" )

computers_move = "rock"

if opponents_move == rock :
    if computers_move == rock :
        print("its a draw!")
    elif computers_move == paper :
        print(f"Computer chose {computers_move} You loose!!!")
    elif computers_move == scissors :
        print(f"Computer chose {computers_move} You Win!!!")
elif opponents_move == scissors :
    if computers_move == rock :
        print(f"Computer chose {computers_move} You loose!!!")
    elif computers_move == paper :
        print(f"Computer chose {computers_move} You Win!!!")
    elif computers_move == scissors :
        print(f"Computer chose {computers_move} Its a draw.")
elif opponents_move == paper :
    if computers_move == rock :
        print(f"Computer chose {computers_move} You Win!!!")
    elif computers_move == paper :
        print("its a draw!")
    elif computers_move == scissors :
        print(f"Computer chose {computers_move} You loose!!!")
else:
    print("invalid!")