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
output_dice = []
for z in range(dice_count) : 
    output_dice.append(random.randint(1 , 6))
# for i in output_dice : 
#     for line in dice_art.get(i) : 
#         print(line)

# for line in range(6) : 
#     for dice in output_dice : 
#         print(dice_art.get(dice)[line] , end = " ")
#     print()

batchsize = 5
for start in range(0 , len(output_dice) , batchsize) : 
    batch = output_dice[start : start + batchsize]
    for line in range(6)  :
        for dice in batch : 
            print(dice_art.get(dice)[line] , end = " ")
        print()
    print()



