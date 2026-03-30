print("Welcome to your shopping cart")
item1 = input("Enter the Name of the item:")
price1 = float(input(f"What is the price of {item1}:"))
print("Ufff thats kinda expenisve!")
quantity1 = float(input(f" How many {item1} you want?:"))
total_price_item_1 = price1 * quantity1
item2 = input("Enter the Name of the next item:")
price2 = float(input(f"What is the price of {item2}:"))
print("Ufff thats kinda expenisve!")
quantity2 = float(input(f" How many {item2} you want?:"))
total_price_item_2 = price2 * quantity2
item3 = input("Enter the Name of the next item:")
price3 = float(input(f"What is the price of {item3}:"))
print("Ufff thats kinda expenisve!")
quantity3 = float(input(f" How many {item3} you want?:"))
total_price_item_3 = price3 * quantity3
grand_total = total_price_item_1 + total_price_item_2 + total_price_item_3
print(f"Your grand total is {grand_total}")