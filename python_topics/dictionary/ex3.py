menu = {
    "burger" : 100 , 
    "chips" : 10 ,
    "water" : 10 ,
    "pizza" : 250 , 
    "taco" : 50 ,
    "fries" : 100
}
orders = []
amounts = []
total = 0
print("----------------------")
for key , value in menu.items() :
    print(f"{key} : {value}" )
print("----------------------")
while True :
    recent_order = input("Enter your order (press q to quit): ").lower().strip()
    if recent_order == "q" : 
        break
    elif menu.get(recent_order) is None :
        continue 
    else :
        orders.append(recent_order)
        amounts.append(menu.get(recent_order))
for amount in amounts :
    total += amount
print("----------------------")
print(f"Your order -  " , end = " ")
for order in orders :
    print(order , end = " ")
print("")
print(f"Your Total is = ${total}")
print("----------------------")



    