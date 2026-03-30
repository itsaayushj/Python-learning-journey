# IF ELIF and ELSE 
print("Lets play GTAV!")
age = int(input("Enter Your age:"))
#if age != int :
 #   print("age should be in number")
    #insted of using int() in 3rd line i tried to put it as a condition in loop hoping it would work..... but i was wrong. it will not crash but everytime it will say its not a number because a input is by default cosidered as string 
if age >= 100 :
    print("You are too old to do these UNC")
elif age >= 18 :
    print("You are officially signed up to kill NPCs!!!")
elif age <= 0 : #we can write infinite elif
    print("Are you sure you are born ? *looks suspeciously*")
else  :  # we wont write age < 18 in else because else means literally anything other than above conditions and we cant add condition in else...for condions use if or elif
    print(" You too young kiddo")
