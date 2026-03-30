import random 
from hangman_words import words
hangman_art = {0:("   ", "   ","   "),
               1 : (" o ","   ","   "),
               2 : (" o "," | ","   "),
               3 : (" o ", "/| ", "   "),
               4 : (" o ","/|\\","   "),
               5 : (" o ", "/|\\", "/  "),
               6 :(" o ", "/|\\", "/ \\")}

is_running = True
while is_running :
    wrong_answers = 0 
    word = random.choice(words)
    guesslist = []
    hint = ["_"] * len(word)
    max_chance = 6 
    while True : 
        print("****************")
        for line in hangman_art[wrong_answers] : 
            print(line)
        print("****************")
        print("|".join(hint))
        user_guess = input('Enter one word you want to guess : ').lower().strip()
        if len(user_guess) != 1  or not user_guess.isalpha() : 
            print("invalid")
            continue
        elif user_guess in guesslist : 
            print("Word is already been guessed!")
        else : 
            guesslist.append(user_guess)
            if user_guess in word : 
                for i in range(len(word)) : 
                    if word[i] == user_guess : 
                        hint[i] = user_guess 
            else : 
                wrong_answers += 1 
                print(f"That was incorrect! You have {max_chance - wrong_answers} Chances remaining")
                if wrong_answers == max_chance : 
                    print("****************")
                    for line in hangman_art[wrong_answers] : 
                        print(line)
                    print("|".join(hint))
                    print("****************")
                    print("You lost ! ")
                    print(f"The word was {word} !")
                    break 
        if "_" not in hint : 
            print("|".join(hint))
            print("You won !")
            break 
