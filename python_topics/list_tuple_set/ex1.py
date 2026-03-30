# shopping cart program 
foods = []
prices = []
total = 0 
while True :
    order = input("Enter the food you want(Q for Quit) : ")
    if order.lower() == "q" :
        break
    else : 
        cost = float(input("Enter the price of the food:"))
        foods.append(order)
        prices.append(cost)

print("---------cart---------")
for food in foods : 
    print(food , end=" ")
for price in prices : 
    total += price
print(f"Your total = ${total}")
    