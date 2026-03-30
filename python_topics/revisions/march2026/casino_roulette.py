#casino rouulette
import random
import time
balance = 100 
red = [1 ,3 ,5 ,7 ,9 ,12 ,14 ,16 , 18 , 19 , 21 , 23 ,25, 27 , 30 , 32 ,34 , 36]
green = 0 

while True :
    magic_number = random.randint(0 , 36)
    bet_choice = input("Which odds you wanna bet on ? press C for colour (2x odds) , press X for Even and  Odd (2x odds) , N for Number (35x odds)").upper()
    if bet_choice == "C" : 
        bet_detail = input("Press R to bet on red and B to bet on black (If its 0 , green then you loose)").upper()
        bet_amount = int(input(f"Your balance is ${balance} , How much you want to bet this round? : "))
        while bet_amount > balance : 
            print("Invalid")
            bet_amount = int(input(f"Your balance is ${balance} , How much you want to bet this round? : "))
        print(f"The dice stopped at {magic_number}")
        if magic_number == 0 :
            print("You loose ")
            balance -= bet_amount 
            print(f"Your balance is {balance}")
            if balance == 0 :
                print("You broke")
                break
            else : 
                    end_or_no  = input("cash out (X) or continue (O) :")
                    if end_or_no == "x" : 
                        print("Cashing out" , end = "")
                        for i in range(5):
                            time.sleep(0.5)
                            print("." , end="")
                        print()
                        print(f"Cashout succeful! ${balance} debited into your account!")
                    else : 
                        continue
        
            if bet_detail == "R" : 
                if magic_number not in red : 
                    print("You loose ")
                    balance -= bet_amount 
                    print(f"Your balance is {balance}")
                    if balance == 0 :
                        print("You broke")
                        break
                    else : 
                        end_or_no  = input("cash out (X) or continue (O) :")
                        if end_or_no == "x" : 
                            print("Cashing out" , end = "")
                            for i in range(5):
                                time.sleep(0.5)
                                print("." , end="")
                            print()
                            print(f"Cashout succeful! ${balance} debited into your account!")
                        else : 
                            continue

            else : 
                print("You won! ")
                balance += (bet_amount)*2 - bet_amount
                print(f"Your balance is {balance}")
                end_or_no  = input("cash out (X) or continue (O) :")
                if end_or_no == "x" : 
                    print("Cashing out" , end = "")
                    for i in range(5):
                        time.sleep(0.5)
                        print("." , end="")
                    print()
                    print(f"Cashout succeful! ${balance} debited into your account!")
                else : 
                    continue
                
        else : 
            print(f"The dice stopped at {magic_number}")
            if magic_number in red or magic_number == 0 : 
                print("You loose ")
                balance -= bet_amount 
                print(f"Your balance is {balance}")
                if balance == 0 :
                    print("You broke")
                    break
                else :
                    end_or_no  = input("cash out (X) or continue (O) :")
                    if end_or_no == "x" : 
                        print("Cashing out" , end = "")
                        for i in range(5):
                            time.sleep(0.5)
                            print("." , end="")
                        print()
                        print(f"Cashout succeful! ${balance} debited into your account!")
                    else : 
                        continue
            else : 
                print("You won! ")
                balance += (bet_amount)*2 - bet_amount
                print(f"Your balance is {balance}")
                end_or_no  = input("cash out (X) or continue (O) :")
                if end_or_no == "x" : 
                    print("Cashing out" , end = "")
                    for i in range(5):
                        time.sleep(0.5)
                        print("." , end="")
                    print()
                    print(f"Cashout succeful! ${balance} debited into your account!")
                else : 
                    continue 
    elif bet_choice == "X" :
        bet_detail = input("Enter E to bet on even and O to bet on odd : ").upper()
        bet_amount = int(input(f"Your balance is ${balance} , How much you want to bet this round? : "))
        while bet_amount > balance : 
            print("Invalid")
            bet_amount = int(input(f"Your balance is ${balance} , How much you want to bet this round? : "))
        if magic_number == 0 :
            even_odd_test = None
            print("You loose ")
            balance -= bet_amount 
            if balance == 0 :
                print("You broke")
                break
            else : 
                end_or_no  = input("cash out (X) or continue (O) :")
                if end_or_no == "x" : 
                    print("Cashing out" , end = "")
                    for i in range(5):
                        time.sleep(0.5)
                        print("." , end="")
                    print()
                    print(f"Cashout succeful! ${balance} debited into your account!")
                else : 
                    continue
        else : 

            if magic_number % 2 == 0 :
                even_odd_test = "E" 
            else : 
                even_odd_test = "O"
        print(f"The dice stopped at {magic_number}")
        if bet_detail == even_odd_test : 
            print("You won! ")
            balance += (bet_amount)*2 - bet_amount
            print(f"Your balance is {balance}")
            end_or_no  = input("cash out (X) or continue (O) :")
            if end_or_no == "x" : 
                print("Cashing out" , end = "")
                for i in range(5):
                    time.sleep(0.5)
                    print("." , end="")
                print()
                print(f"Cashout succeful! ${balance} debited into your account!")
            else : 
                continue
        else :  
            print("You loose ")
            balance -= bet_amount 
            if balance == 0 :
                print("You broke")
                break
            else : 
                end_or_no  = input("cash out (X) or continue (O) :")
                if end_or_no == "x" : 
                    print("Cashing out" , end = "")
                    for i in range(5):
                        time.sleep(0.5)
                        print("." , end="")
                    print()
                    print(f"Cashout succeful! ${balance} debited into your account!")
                else : 
                    continue
    elif bet_choice == "N" :
        bet_detail = int(input("Enter the number between 0 and 36 : "))
        bet_amount = int(input(f"Your balance is ${balance} , How much you want to bet this round? : "))
        while bet_amount > balance : 
            print("Invalid")
            bet_amount = int(input(f"Your balance is ${balance} , How much you want to bet this round? : "))
        print(f"The dice stopped at {magic_number}")
        if bet_detail == magic_number : 
            print("You won! ")
            balance += (bet_amount)*35 - bet_amount
            print(f"Your balance is {balance}")
            end_or_no  = input("cash out (X) or continue (O) :")
            if end_or_no == "x" : 
                print("Cashing out" , end = "")
                for i in range(5):
                    time.sleep(0.5)
                    print("." , end="")
                print()
                print(f"Cashout succeful! ${balance} debited into your account!")
            else : 
                continue
        else : 
            print("You loose ")
            balance -= bet_amount 
            if balance == 0 :
                print("You broke")
                break
            else :
                end_or_no  = input("cash out (X) or continue (O) :")
                if end_or_no == "x" : 
                    print("Cashing out" , end = "")
                    for i in range(5):
                        time.sleep(0.5)
                        print("." , end="")
                    print()
                    print(f"Cashout succeful! ${balance} debited into your account!")
                else : 
                    continue 