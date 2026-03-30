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
for dice in range(dice_count) : 
    output_dice.append(random.randint(1 , 6)) 

# for line in range(6) : 
#     for dice in output_dice : 
#         print(dice_art.get(dice)[line] , end = "")
#     print()

#  batching...
batch_size = 5 # for eg     
for start in range(0 , len(output_dice) , batch_size) : 
    batch = output_dice[start : start + batch_size]
    for line in range(6) : 
        for dice in batch : 
          print(dice_art.get(dice)[line] , end = " ")
        print()
    print()

for nums in output_dice : 
    total += nums 

print(f"The total is {total}")
