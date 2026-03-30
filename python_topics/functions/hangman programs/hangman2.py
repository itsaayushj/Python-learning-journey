word = "elephant"
hint = ["_"] * len(word)
guesslist = list()
wrong_guess = 0 
hangman_art = {0:("   ", "   ","   "),
               1 : (" o ","   ","   "),
               2 : (" o "," | ","   "),
               3 : (" o ", "/| ", "   "),
               4 : (" o ","/|\\","   "),
               5 : (" o ", "/|\\", "/  "),
               6 :(" o ", "/|\\", "/ \\")}
while True : 
    print("**************************")
    for line in hangman_art[wrong_guess] : 
        print(line)
    print("**************************")
    print(" ".join(hint))
    guess = input("Enter one letter : ").lower().strip()
    if len(guess) > 1 or guess in guesslist:
        print("ERROR! Either the guess is invalid or you have already guessed it!")
        continue
    else : 
        guesslist.append(guess)
        if guess in word : 
            for i in range(len(word)) : 
                if word[i] == guess : 
                    hint[i] = guess 
        else : 
            wrong_guess += 1 
            print("Wrong guess ")
        if "_" not in hint : 
            print(" ".join(hint))
            print("You won !") 
            break
        elif wrong_guess >= 6 : 
            print("**************************")
            for line in hangman_art[wrong_guess] : 
                print(line)
            print("**************************")
            print(f"You lost the word was {word}")
            break