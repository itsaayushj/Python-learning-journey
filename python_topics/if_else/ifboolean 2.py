print("Lets try to run if else with boolean variables")
demand = input("What doyou want to buy (Apple/Orange/Melon):")
apple = False
orange = False
melon = True
apple_quantity = 0
total_price_apple = 0
total_price_orange = 0
orange_quantity = 0
total_price_melon = 0
melon_quantity = 0

if demand =="apple":
    if apple :
        apple_quantity = int(input("How many apple do you want? (10$ per piece)"))
        total_price_apple = apple_quantity * 10
    else :
        print("No apple in stock")
if demand == "orange":
    if orange :
        orange_quantity = int(input("How many orange do you want? (20$ per piece)"))
        total_price_orange = orange_quantity * 10
    else :
        print("No orange in stock")
elif demand == "melon":
    if melon :
        melon_quantity = int(input("How many melon do you want? (18$ per piece)"))
        total_price_melon = melon_quantity * 18
    else :
        print("No melon in stock")
else :
    print("No items found")

grand_total = total_price_apple + total_price_melon + total_price_orange

print(f"Your grand total is : $ {grand_total}")