# number gusser
import random 
guess_count = 0
magic_number = random.randint(1, 100)
user_guess = int(input("Enter your guess : "))
while True :
    if user_guess > 100 or user_guess < 0:
        print("invalid guess")
        user_guess = int(input("Enter your guess : "))
        continue
    if user_guess > magic_number : 
        print("Guess too big")
        guess_count += 1
        user_guess = int(input("Enter your guess : "))
    elif user_guess < magic_number : 
        print("Guess too small ")
        guess_count += 1
        user_guess = int(input("Enter your guess : "))
    else : 
        print("Correct guess")
        guess_count += 1
        print(f"You guessed it in {guess_count} guesses!")
        break 


