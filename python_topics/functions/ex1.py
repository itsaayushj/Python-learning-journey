# 05:24:00 exercise bro code

account_database = {
100 : "pizza" , 101 : "pasta" , 102 : "burger" , 103 : "taco"
}
balance_database = {
    100 : 1000 , 101 : 50 , 102 : 10000 , 103 : 999
}
user_balance = None
def account_checker() : 
    attemt_counter = 0 
    user_account = int(input("Enter your account no : "))
    while user_account not in account_database : 
        print("Invalid account number. Please try again ")
        user_account = int(input("Enter your account no : "))
    else : 
        user_password = input("Enter your password : ")
        while  user_password != account_database.get(user_account) :
            attemt_counter +=1 
            print(f"Wrong password. You have used {attemt_counter} out of  5 attempts ")
            if attemt_counter == 5 : 
                print("Too many wrong attemps. Try again later . BYE!")
                exit()
            user_password = int(input("Enter your account password : "))
        else : 
            print("Account Verified!")
    return balance_database.get(user_account) , user_account

def withdraw_system(user_balance):
    withdraw_amount = int(input("Enter the amount you want to withdraw : "))
    while withdraw_amount > user_balance : 
        print("You dont have enough balance !")
        withdraw_amount = int(input("Enter the amount you want to withdraw : "))
    else : 
        user_balance -= withdraw_amount 
        print(f"Your current balance is {user_balance}")
    return user_balance

    

def deposit_system(user_balance):
    deposit_amount = int(input("Enter the amount you want to deposit : "))
    user_balance += deposit_amount 
    print(f"Your current balance is {user_balance}")
    return user_balance

 

def main() : 
    
    user_balance , user_account = account_checker()
    user_choice = input("Enter X to withdraw and Y to deposit : ").lower().strip()
    while user_choice != "x" and user_choice  != "y" : 
        print("Invalid choice")
        user_choice = input("Enter X to withdraw and Y to deposit : ").lower().strip()
    match user_choice :
        case "x" : 
           user_balance =  withdraw_system(user_balance)
        case "y" : 
            user_balance = deposit_system(user_balance)
    balance_database[user_account] = user_balance 


if __name__ == '__main__' : 
    main()
else : 
    print("Tf you are importing this for ?")

            