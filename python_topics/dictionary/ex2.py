menu = {
    "pedri" : 10.00 ,
    "lamine" : 20.00 , 
    "vini jr" : 100 , 
    "ten hag" : 1.00 , 
    "palmer" : 50 
}
order = []
amount = []
total = 0
print("-----------------------------")
for item , value in menu.items() :
    print(f"{item} : {value}")
print("-----------------------------")
while True :
    user_input = input("Enter your order....press q to quit : ").lower().strip()
    if user_input == "q" :
        break
    elif menu.get(user_input) is None:
        continue 
    else : 
        order.append(user_input)

for items in order :
    amount.append(menu.get(items))

for money in amount :
    total += money 

print("YOUR ORDER -")
for i in order :
    print(i , end=" ")
print("")
print(f"Your total - {total}")
