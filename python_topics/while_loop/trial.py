# while loop excecute some code WHILE the condition remains true 

age = int(input("Enter your age :"))

while age <= 0 or age > 100 :
    print("Who are you kidding to ? Just enter your age lil bro!")
    age = int(input("Enter your age :"))  # remove this line and it will go to infinite loop 💀

print("Thanks for entering your age !")
print(f"You are {age} Years old!")

