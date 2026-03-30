print(" Lets guess the magic number ")
magic_number = 939
guess = int(input(" Enter the magic number :"))
difference = magic_number - guess
while not magic_number == guess :
    print(" Nope you are wrong lmao")
    difference = magic_number - guess
    if difference < -10 :
        print("Guess was Too High !!!")
    elif difference < 0 :
        print("Guess was High!")
    elif difference > 10 :
        print("Guess was Too low !!")
    elif difference > 0 :
        print("Guess was Low!")
    else :
        print(" How did you even end up here? ")
    guess = int(input(" Enter the magic number :"))
print(f"Congratulations you guessed it right the number was {magic_number}")

