print("lets calculate compound intrest")
principal = float(input("Enter the principal:"))
intrest_rate = float(input("Enter the Intrest Rate:"))
time = float(input("Enter the Time (in years):"))
a = principal * ((1 + intrest_rate/100)**time)
intrest_earned = a - principal 
print(f"total amount after {time} year is : ${round(a , 2)}")
print(f"Intrest earned in {time} is : ${round(intrest_earned , 2)}")