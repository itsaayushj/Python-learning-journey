import random
from hangman_words import words
hangman_art = {0:("   ", "   ","   "),
               1 : (" o ","   ","   "),
               2 : (" o "," | ","   "),
               3 : (" o ", "/| ", "   "),
               4 : (" o ","/|\\","   "),
               5 : (" o ", "/|\\", "/  "),
               6 :(" o ", "/|\\", "/ \\")}
def game_running_check() : 
    gamerun_choice = input("Enter x to play again and anything else to quit").lower().strip()
    if gamerun_choice == "x" : 
        is_running = True
    else : 
        is_running = False 
    return is_running
is_running = True
while is_running : 
    word = random.choice(words)
    hint = ["_"] * len(word)
    guess_list = list()
    wrong_answers = 0 
    while True : 
        print("***************")
        for line in hangman_art[wrong_answers] : 
            print(line)
        print("***************")
        print("|".join(hint))

        user_guess = input("Enter one letter : ").strip().lower()
        if len(user_guess) > 1 or user_guess.isalpha() == False : 
            print("Invalid!")
            continue 
        elif user_guess in guess_list : 
            print("You have already guessed this letter before.")
            continue
        else : 
            guess_list.append(user_guess)
            if user_guess in word : 
                for i in range(len(word)) : 
                    if word[i] == user_guess : 
                        hint[i] = user_guess 
            elif user_guess not in word : 
                wrong_answers += 1 
                if wrong_answers >= 6 : 
                    print("***************")
                    for line in hangman_art[6] : 
                        print(line)
                    print("***************")
                    print("You lost !")
                    print(f"The answer was {word}")
                    is_running = game_running_check()
                    break
                else : 
                    print(f"Wrong guess ! You have {6 - wrong_answers} chance left ")
        
        if hint.count("_") == 0 :
            print("You won !")
            
            is_running = game_running_check()
            break