og_menu = {
    "popcorn" : 1.00 ,
    "hot dog" : 2.00 , 
    "asst candy" : 2.00 , 
    "soda" : 1.00 ,
    "bottled water" : 1.00
}
orders = []
amounts = []
total = 0
while True :
    latest_order = input("Enter your order (q to end): ").lower().strip()
    if latest_order == "q" :
        break
    elif og_menu.get(latest_order) is None :
        continue
    else : 
        orders.append(latest_order)
        amounts.append(og_menu.get(latest_order))

for amount in amounts : 
    total += amount 

print("Your order - " , end = " ")
for order in orders : 
    print(order , end = " ")
print(" ")
print(f"Your total : {total}")

