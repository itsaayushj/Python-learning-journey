print("This is a shopping cart")
item_one = input("Enter item one")
item_one_price = float(input("Enter price of item one")) 
#assuming user might use "$10.99" not just "11$" so preventing error
item_one_quantity = float(input("Enter the quantity of item one")) 
#same here eg- 0.500 kg (broke ass user) 
item_two = input("Enter item two")
item_two_price = float(input("Enter price of item two"))
item_two_quantity = float(input("Enter the quantity of item two"))
item_three = input("Enter item three")
item_three_price = float(input("Enter price of item three"))
item_three_quantity = float(input("Enter the quantity of item three"))
item_one_total = item_one_price * item_one_quantity
item_two_total = item_two_price * item_two_quantity
item_three_total = item_three_price * item_three_quantity
total_price = item_one_total + item_two_total + item_three_total
print(f"The total of {item_one} is {item_one_total}")
print(f"The total of {item_two} is {item_two_total}")
print(f"The total of {item_three} is {item_three_total}")
print(f"The total bill of your shopping is {total_price}")
