# functions = A block of reusable code 
#             place () after the function name to invoke it  
def lol() : 
    print("hahahahaahaha")

# lol()
# lol()
# lol()

def hello_there(your_name , age ) : 
    print(f"Hello {your_name}")
    print(f"You are {age} years old")
hello_there("aayush" , 19)

def invoice(name , amount, due_date) : 
    amount = float(amount)
    print(f"Hi {name}")
    print(f"your total bill is ${amount:.2f}")
    print(f"It is due on {due_date}")

invoice("aayush" , "100.833" , "1/1/26")

