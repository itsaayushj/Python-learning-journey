questions = ( "Total Elements in periodic table :" ,
"Which animal lays the largest egg ? :" ,
"what is the most abundant gas in the earth's atmosphere?:" , 
"How many bones are there in a human body ? " ,
"Which is the hottest planet in the solar system ?"

)
options = ( 
    (
        "A - idk " ,
        "B - infinite" ,
        "C - Elon Musk" ,
        "D - 118" ) ,
    (
        "A - ant" ,
        "B - peppa pig" ,
        "C - garfield" ,
        "D - mr. ostrich" 
    ) ,
    (
        "A - Your fart" ,
        "B - nitrogen" ,
        "C - pollution" ,
        "D - how tf i am supposed to know that?"
    ) ,
    (
        "A - infinite" ,
        "B - 206" ,
        "C - lemme check real quick" ,
        "D - I got no bones only muscles "
    ) ,
    (
        "A - venus" ,
        "B - uranus hehe" ,
        "C - florida" ,
        "D - volcano"

    )
)
question_number = 0 
answers = ["D" , "D" , "B" , "B" , "A" ]
guesses = []
score = 0
for question in questions : 
    print(question )
    for option in options[question_number] : 
        print(option )
    user_answer = input("Enter your answer (A B C D) : ").upper().strip()
    guesses.append(user_answer)
    if user_answer == answers[question_number] :
        print("You are corect ")
        score += 1
    else : 
        print(f"You are wrong. Correct answer was {answers[question_number]}")

    question_number += 1

print("Your guesses were - " , end = " ")
for guess in guesses : 
    print(guess , end = " " )
print("")
print("correct answers were - " , end = " ")
for answer in answers : 
    print(answer , end = " " )
print("")
percentage = score / len(questions) * 100
print(f"That is %{percentage}")

