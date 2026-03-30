import random
game_on = True  
guess_counter = 0 
while True : 
    print("Welcome to magic number game ! ")
    lowest_range = int(input("Enter the lowest number "))
    highest_range = int(input("Enter the highest number"))
    magic_number = random.randint(lowest_range , highest_range)
    while game_on : 
        user_guess = int(input("Enter your guess : "))
        if lowest_range <= user_guess <= highest_range : 
            if user_guess > magic_number : 
                print("Guess too big ")
                guess_counter += 1 
            elif user_guess < magic_number : 
                print("Guess too small ")
                guess_counter += 1
            else : 
                print("correct guess ! ")
                guess_counter += 1
                
                print(f"you guessed it in {guess_counter} guesses")
                end_or_no = input("press Y to play again N to quit ").strip().lower()
                while end_or_no != "y" and end_or_no != "n" : 
                    print("invalid ")
                    end_or_no = input("press Y to play again N to quit ").strip().lower()
                if end_or_no == "y" : 
                    print("starting a new game !")
                    guess_counter = 0 
                    magic_number = random.randint(lowest_range , highest_range)
                    continue 
                else : 
                    game_on = False  
        else : 
            print("invalid, out of range! ") 
    quit() # can use break to end it but just doing it because i just learned about quit() , it just directly ends the whole program   


        
        
