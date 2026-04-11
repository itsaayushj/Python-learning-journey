import random 
dice_art = {
    1 : ("┌─────────┐" , 
         "│         │" , 
         "│    o    │" , 
         "│         │" , 
         "│         │" ,
         "└─────────┘" ) , 
    2 : ("┌─────────┐" , 
         "│  o      │" , 
         "│         │" , 
         "│         │" , 
         "│      o  │" ,
         "└─────────┘" ) ,
    3 : ("┌─────────┐" , 
         "│         │" , 
         "│  o      │" , 
         "│    o    │" , 
         "│      o  │" ,
         "└─────────┘" ) , 
    4 : ("┌─────────┐" , 
         "│ o       │" , 
         "│  o      │" , 
         "│    o    │" , 
         "│      o  │" ,
         "└─────────┘" ) , 
    5 : ("┌─────────┐" , 
         "│ o       │" , 
         "│  o   o  │" , 
         "│    o    │" , 
         "│      o  │" ,
         "└─────────┘" ) , 
    6 : ("┌─────────┐" , 
         "│ o   o   │" , 
         "│  o      │" , 
         "│    o  o │" , 
         "│      o  │" ,
         "└─────────┘" )
}
total = 0 
dice_count = int(input("Enter number of dice you want : "))
if dice_count >= 11 : 
    batch_count = int(input("Thats a lot of dice! how many dice you want in a batch ? : "))
else : 
    batch_count = dice_count 
output_dice = []
for dice in range(dice_count) : 
    output_dice.append(random.randint(1,6))
for num in output_dice : 
    total += num 
for start in range(0 , len(output_dice) , batch_count) : 
    batch = output_dice[start : start + batch_count]
    for line in range(6) : 
        for dice in batch : 
            print(dice_art.get(dice)[line] , end = " ")
        print()
    print()
    