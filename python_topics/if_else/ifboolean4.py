
# IT is whith ai ( i dont understand it yet)

print("Let's try to run if else with boolean variables")


demand = input("What do you want to buy? (Apple Orange Melon) - separate items with spaces: ").lower().split()

# Stock availability
apple = False
orange = False
melon = True

# Initialize quantities and totals
apple_quantity = 0
total_price_apple = 0
orange_quantity = 0
total_price_orange = 0
melon_quantity = 0
total_price_melon = 0

# Check if apple is in the demand list
if "apple" in demand:
    if apple:
        apple_quantity = int(input("How many apples do you want? ($10 per piece): "))
        total_price_apple = apple_quantity * 10
    else:
        print("No apple in stock")

# Check if orange is in the demand list
if "orange" in demand:
    if orange:
        orange_quantity = int(input("How many oranges do you want? ($20 per piece): "))
        total_price_orange = orange_quantity * 20
    else:
        print("No orange in stock")

# Check if melon is in the demand list
if "melon" in demand:
    if melon:
        melon_quantity = int(input("How many melons do you want? ($18 per piece): "))
        total_price_melon = melon_quantity * 18
    else:
        print("No melon in stock")

# Calculate the grand total
grand_total = total_price_apple + total_price_orange + total_price_melon

print(f"\nYour grand total is: ${grand_total}")
print("Thank you! Visit us again!")