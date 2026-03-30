import random 
from hangman_words import words

hangman_art = {0:("   ", "   ","   "),
               1 : (" o ","   ","   "),
               2 : (" o "," | ","   "),
               3 : (" o ", "/| ", "   "),
               4 : (" o ","/|\\","   "),
               5 : (" o ", "/|\\", "/  "),
               6 :(" o ", "/|\\", "/ \\")}

def display_man(wrong_answers) : 
    print("****************")
    for line in hangman_art[wrong_answers] :
        print(line) 
    print("****************")
        
def display_hint(answer , new_guess , hint ):  
    print(hint)
    if new_guess in answer : 
        for i in range(len(answer)) : 
            if answer[i] == new_guess : 
                hint[i] = new_guess 
    return hint
def display_answer(answer):
    print(f"The answer was {answer}!")

def main():
    answer = random.choice(words)
    wrong_answers = 0
    is_on = True
    new_guess = ""
    user_guesslist = []
    hint = list()
    while is_on :
        display_man(wrong_answers)
        for word in answer : 
            hint.append("_")
        hint = display_hint(answer , new_guess , hint )
        new_guess = input("Enter one word which you think is inside the answer : ")
        if new_guess in user_guesslist : 
            print("The word has already been guessed!")
            continue
        elif len(new_guess) > 1 : 
            print("invalid")    
            continue
        if new_guess not in answer : 
            wrong_answers += 1 
        user_guesslist.append(new_guess)
        if wrong_answers >= len(hangman_art) -1 : 
            display_answer(answer)

if __name__ == '__main__' : 
    main()
