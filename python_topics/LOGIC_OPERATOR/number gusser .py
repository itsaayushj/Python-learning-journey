print("Lets guess number (upto 100)")
secret_number = 69 
guess = int(input("Enter your guess :"))
if guess > 100 : 
    print("Number is over 100")
elif guess < 0 :
    print("Number cant be negative")
else :
    difference = secret_number - guess
    if difference == 0 :
        print(f"Guess was Perfect!!!! The number was {secret_number}")
    elif difference < -10 :
        print("Guess was Too High !!!")
    elif difference < 0 :
        print("Guess was High!")
    elif difference > 10 :
        print("Guess was Too low !!")
    elif difference > 0 :
        print("Guess was Low!")
    else :
        print(" How did you even end up here? ")


