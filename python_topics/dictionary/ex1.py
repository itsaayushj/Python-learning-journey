og_menu = {
    "popcorn" : 1.00 ,
    "hot dog" : 2.00 , 
    "asst candy" : 2.00 , 
    "soda" : 1.00 ,
    "bottled water" : 1.00
}
order = []
print("Welcome to our hotel!")
print("Here's our small menu :")
print("-------------------------")
for item , price in og_menu.items() :
    print(f"{item} ----- {price}")
print("-------------------------")
while True:
    new_order = input("Place your order : ").lower().strip()
    check = og_menu.get(new_order)
    if new_order == "q":
        break
    elif check is not None  :
        order.append(new_order)
    else :
        continue
bill_price = []
for item in order :
    bill_price.append(og_menu.get(item))
total = 0
for amount in bill_price :
    total += amount 
print(f"Your order - {order}")
print(f"Your Total - {total}")



