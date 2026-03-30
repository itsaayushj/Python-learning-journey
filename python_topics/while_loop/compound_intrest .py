print("lets calculate compound intrest")
principal = float(input("Enter the principal:"))
while principal <= 0 :
    print("Principal cant be 0 or negative!")
    principal = float(input("Enter the principal:"))
intrest_rate = float(input("Enter the Intrest Rate:"))
while intrest_rate <= 0 :
    print("Intrest rate cant be 0 or negative")
    intrest_rate = float(input("Enter the Intrest Rate:"))
time = float(input("Enter the Time (in years):"))
while time <= 0 :
    print(" Time cant be negative or 0. What is this? intersteller? ")
    time = float(input("Enter the Time (in years):"))
final_amount = principal * ((1 + intrest_rate/100)**time)
intrest_earned = final_amount - principal 
print(f"total amount after {time} year is : ${final_amount:.2f}")
print(f"Intrest earned in {time} is : ${intrest_earned:.2f}")