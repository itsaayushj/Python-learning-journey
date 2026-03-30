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
output_dice = [] 
user_input = int(input("Enter the amount of dice you want  :"))
for x in range(user_input) : 
    output_dice.append(random.randint(1,6))
for x in output_dice : 
    total += x 

# for dice in output_dice : 
#     for line in dice_art.get(dice) : 
#         print(line )
    
# for line in range(6) : 
#     for dice in output_dice :
#         print(dice_art.get(dice)[line] , end = " ")
#     print()
    
batch_size = 10 

for start in range(0 , len(output_dice) , batch_size) : 
    batch = output_dice[start : start + batch_size] 
    for line in range(6) : 
     for dice in batch :
         print(dice_art.get(dice)[line] , end = " ")
     print()

