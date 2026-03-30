# the other way of ex1 
#  the way bro code did 

account_database = {
100 : "pizza" , 101 : "pasta" , 102 : "burger" , 103 : "taco"
}
balance_database = {
    100 : 1000 , 101 : 50 , 102 : 10000 , 103 : 999
}

def verify_user() : 
    user_account = int(input("Enter your account number : "))
    while  user_account not in account_database : 
        print("Invalid account number !")
        user_account = int(input("Enter your account number : "))
    user_password = input("Enter your password : ")
    attempt_counter = 0 
    while user_password != account_database.get(user_account) : 
        attempt_counter += 1 
        if attempt_counter == 5 : 
            print("Too many wrong attempt! Come back later")
            exit()
        else : 
            print(f"Invalid Password ! {attempt_counter} / 5 attempt used")
            user_password = input("Enter your password : ")
    return balance_database.get(user_account) , user_account 
        

def show_balance(user_balance) : 
    print(f"Your balance is $ {user_balance:.2f}")

def deposit_system(user_balance) : 
    deposit_amount = float(input("Enter the amount you want to deposit : "))
    user_balance += deposit_amount 
    print(f"Your current balance is {user_balance}")
    return user_balance

def withdraw_system(user_balance) : 
    withdraw_amount = float(input("Enter the amount you want to withdraw : "))
    while withdraw_amount > user_balance : 
        print("You dont have enough balance !")
        withdraw_amount = float(input("Enter the amount you want to withdraw : "))
    else : 
        user_balance -= withdraw_amount 
        print(f"Your current balance is {user_balance}")
    return user_balance

def account_transfer(user_balance , user_account) : 
    receiver_side = int(input("Enter the account you want to send money to : ")) # too bored to check if the account no is right or no , i assume user has braincells 
    sendable_amount = float(input("Enter the amount of money you want to send :  "))
    while sendable_amount > user_balance : 
        print("Invalid balance!")
        sendable_amount = float(input("Enter the amount of money you want to send :  "))
    user_balance -= sendable_amount 
    balance_database[user_account] = user_balance
    balance_database[receiver_side] += sendable_amount
    return user_balance 
    
def main() : 
    user_balance , user_account = verify_user()
    is_running = True
    while is_running : 
        print("----------------------------------")
        print("Welcome to the Gotham central bank !")
        print("----------------------------------")
        print("1.SEE BALANCE")
        print("2.DEPOSIT CASH")
        print("3.WITHDRAW CASH")
        print("4.ONLINE TRANSFER")
        print("5.EXIT")
        print("----------------------------------")
        user_choice = int(input("Enter 1-5 : "))
        if user_choice not in [1 , 2, 3 ,4, 5 ] : 
            print("invalid")
            user_choice = int(input("Enter 1-5 : "))
        match user_choice : 
            case 1 : 
                show_balance(user_balance)
            case 2 : 
                user_balance = deposit_system(user_balance)
                balance_database[user_account] = user_balance
            case 3 : 
                user_balance = withdraw_system(user_balance)
                balance_database[user_account] = user_balance
            case 4 : 
                user_balance = account_transfer(user_balance , user_account) 
                balance_database[user_account] = user_balance
            case 5 : 
                is_running = False


if __name__ == "__main__" : 
    main()