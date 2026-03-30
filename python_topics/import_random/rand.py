import random

magic_number = random.randint(1, 100)
counter = 1
while True :
    guess = int(input("Enter your guess , (between 1 - 100) :"))
    if guess == magic_number :
        print(f"Correct, you done it in {counter} guesses")
        break 
    elif guess > magic_number : 
        print("Your guess was Higher!")
        counter += 1 
    elif guess < magic_number : 
        print("Your guess is lower !")
        counter += 1 

