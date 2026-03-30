print("Lets try to run if else with boolean variables")
demand = input("What doyou want to buy (Apple/Orange/Melon):")
apple = False
orange = False
melon = True
if demand =="apple":
    if apple :
        print("Apple is in stock")
        apple_quantity = int(input("How many apple you want to buy ($3.50 per piece)"))
        total_price_apple = apple_quantity * 3.50
        print(f"Your total will be {total_price_apple}")
    else :
        print("No apple today")
elif demand =="orange":
    if orange :
        print("orange is in stock")
        orange_quantity = int(input("How many orange you want to buy"))
        total_price_orange = orange_quantity * 7.99
        print(f"Your total will be {total_price_orange}")
    else :
        print("No orange today")
elif demand =="melon":
    if melon :
        print("Melon is in stock ($7.99 per piece)")
        melon_quantity = int(input("How many melon you want to buy"))
        total_price_melon = melon_quantity * 7.99
        print(f"Your total price for melon will be {total_price_melon}")

    else :
        print("No Melon today")
else :
    print("Item not found")

 #grand_total = total_price_apple + total_price_melon + total_price_orange    (this shit wont work because we declared variables in a if else statment and if the condition in if else is not fulfilled it will never run so python doesnt know this avriable exists)
#print(f"Your Grand total is : ${grand_total}")
print("visit us again!")
