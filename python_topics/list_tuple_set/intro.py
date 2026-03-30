# collection = single "variable" used to store multiple values 
# list = [] orderd and unchanged , duplicates are okay .
# set = {} unorderd and mutable . add / remove okay. No duplicates
# Tuple = () ordered and unchangable. Duplicates OK , Faster.

players = ["Messi" , "Ronaldo" , "Lewa" , "lamine", "Pedri"]
print(len(players))
print("Pedri" in players)
players[0] = "lukaku"
players.append("neymar")
players.remove("lukaku")
# for player in players :
#     print(player)
players.insert(0 , "Messi")
print(players)
players.sort() # sort alphabetically
print(players.reverse()) # reversed by index
players.count("Messi") # counts dublicates 
