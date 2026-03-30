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
answers = ("D" , "D" , "B" ,"B" , "A")
guesses = []   
question_no = 0
score = 0
for question in questions :
    print("--------------------------------")
    print(question)
    for option in options[question_no] :
        print(option)
    user_guess = input("Enter your guess (A B C D) :").upper()
    guesses.append(user_guess)
    if user_guess == answers[question_no] :
        print("correct!")
        score += 1
    else :
        print("Incorrect")
        print(f"{answers [question_no] } was the correct answer!")

        
    question_no += 1
percentage = (score / question_no ) * 100
print("--------------------------------")
print("YOUR RESULT !")
print("CORRECT ANSWERS WERE -")
for answer in answers :
    print(answer, end=" ")
print("YOUR GUESSES WERE -")
for guess in guesses :
    print(guess , end=" ")
print(f"your total score is {score}")
print(f"That is {percentage} %")
print("--------------------------------")