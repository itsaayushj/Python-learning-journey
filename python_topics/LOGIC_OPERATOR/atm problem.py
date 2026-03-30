print("Welcome to ATM") 
# pin and balance
pin1 = 6969
pin2 = 1234
pin3 = 9876
pin4 = 0000
pin1_bal = 9999
pin2_bal = 7500
pin3_bal = 0
pin4_bal = 250

input_pin = int(input("Enter your pin:"))

if input_pin == pin1 : 
    withdraw_bal = float(input("Enter the amount you want to withdraw:"))
    if withdraw_bal <= pin1_bal:
        print("Withdrawl successful!")
        pin1_bal = pin1_bal - withdraw_bal
        print(f"Your current balance is {pin1_bal}")
    else : 
        print("insufficient balance!")

elif input_pin == pin2 :
    withdraw_bal = float(input("Enter the amount you want to withdraw:"))
    if withdraw_bal <= pin2_bal :
        print("Withdrawl successful!")
        pin2_bal = pin2_bal - withdraw_bal
        print(f"Your current balance is {pin2_bal}")
    else : 
        print(" Insufficient balance")

elif input_pin == pin3 :
    withdraw_bal = float(input("Enter the amount you want to withdraw:"))
    if withdraw_bal <= pin3_bal :
        print("Withdrawl successful!")
        pin3_bal = pin3_bal - withdraw_bal
        print(f"Your current balance is {pin3_bal}")
    else : 
        print(" Insufficient balance")

elif input_pin == pin4 :
    withdraw_bal = float(input("Enter the amount you want to withdraw:"))
    if withdraw_bal <= pin4_bal :
        print("Withdrawl successful!")
        pin4_bal = pin4_bal - withdraw_bal
        print(f"Your current balance is {pin4_bal}")
    else : 
        print(" Insufficient balance")

else :
    print(" Pin number is not recognised!!! Check and try again")

        
        








