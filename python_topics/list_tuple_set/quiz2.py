questions = (
    (
        "What is the capital of Japan?"
    ) ,
    (
        "Which planet is known as the Red Planet? "
    ) , 
    (
        "Who invented Python programming language?"
    ) 
)
options = (
    (
        " A -Tokyo" , 
        " B - Moscow" ,
        " C - Oslo"
        
    ) , 
    (
        " A - Earth" ,
        " B - Mars" ,
        " C - uranus"
        
    ) ,
    (
        " A - Harry potter" ,
        " B - Amy Santiago" ,
        " C - Guido van Rossum"
        
    )
)
question_number = 0
guesses = []
answers = ("A" , "B" , "C")
score = 0
for question in questions :
    print("--------------------------")
    print(question)
    print("")
    for option in options[question_number]:
        print(option )
    user_guess = input("Enter your guess (A ,B , C) :").upper()
    guesses.append(user_guess)
        
    if user_guess == answers[question_number] :
            print("Correct!")
            score += 1
    else : 
            print("Incorrect!")
            print(f"{answers [question_number]} was the correct option")
    question_number += 1

print("--------------------")
print("Result!")
print("Your guesses were - ")
for guess in guesses :
    print(guess , end=" ")
print("correct answere were -")
for answer in answers :
    print(answer , end=" ")
print(" ")
percentage = score / len(questions) *100 
print(f"Your total score was {score}")
print(f"That is {percentage:2f} %")

