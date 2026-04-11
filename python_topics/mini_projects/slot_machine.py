import random
import time

symbols =  ["🍃" , "🍂" , "🍀" , "🌿" , "🍁"]
def spin_row(user_balance) :
    print("----------------------------------")
    print("THE SYMBOLS ARE : 🍃 🍂 🍀 🌿 🍁")
    print("----------------------------------")
    print(f"Your balace is : ${user_balance}")
    user_bet = float(input("Enter the amount you want to bet! (25x odds ) : "))
    while user_bet > user_balance :
        print("Invalid funds!")
        user_bet = float(input("Enter the amount you want to bet! (25x odds ) : "))
    user_balance-= user_bet
    print("Spinning the slot" , end="")
    for x in range(5) : 
        print("." , end="")
        time.sleep(0.5)
    print("")
    slot_result = []
    slot_result.append(random.choice(symbols))
    slot_result.append(random.choice(symbols))
    slot_result.append(random.choice(symbols))
    return slot_result , user_bet , user_balance
def print_row(slot_result) : 
    print(f"THE SLOT RESULTS ARE : {slot_result[0]} | {slot_result[1]} | {slot_result[2]}") # can also do "|".join(slot_result)
    
def get_payout(slot_result, user_bet , user_balance) : 
    if slot_result[0] == slot_result[1] == slot_result[2] : 
        print("You won!!!!")
        user_bet *= 25
        print(f"You just won ${user_bet:.2f}")
        user_balance += user_bet
    else : 
        print("Sorry you lost!")
    return user_balance
def main() : 
    is_on = True
    user_balance = 100
    while is_on :
        slot_result , user_bet , user_balance =  spin_row(user_balance)
        print_row(slot_result)
        user_balance = get_payout(slot_result, user_bet , user_balance)
        if user_balance == 0 : 
            print("You went bankrupt! BYE!")
            break
        else : 
            on_or_no = input("X to play again and Y to end : ").lower().strip ()
            if on_or_no != "x" and on_or_no != "y" : 
                print("Invalid choice! leaving the program !")
                break 
            elif on_or_no == "x" : 
                continue 
            else : 
                break 

if __name__ == "__main__" : 
    main() 
