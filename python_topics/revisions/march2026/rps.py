# rock paper scissors 
import random 
choices = ["rock" , "paper" , "scissors"]
user_choice = input("Enter your choice : ").strip().lower()
while user_choice not in choices : 
    print("Invalid")
    user_choice = input("Enter your choice : ").strip().lower()
computer_choice = random.choice(choices)

if (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock") : 
    print("User lost !")
elif user_choice == computer_choice : 
    print("Its a draw!")
else : 
    print("User won ")
    
