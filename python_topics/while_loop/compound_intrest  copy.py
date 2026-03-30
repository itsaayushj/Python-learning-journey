print("lets calculate compound intrest")
while True :
    principal = float(input("Enter the principal : "))
    if principal < 0 :
        print("Principal cant be negative")
    else :
        break

while True :
    intrest_rate = float(input("Enter the intrest rate : "))
    if intrest_rate < 0 :
        print("intrest rate cant be negative")
    else :
        break

while True :
    time = float(input("Enter the time : "))
    if time < 0 :
        print("time cant be negative")
    else :
        break


final_amount = principal * ((1 + intrest_rate/100)**time)
intrest_earned = final_amount - principal 
print(f"total amount after {time} year is : ${final_amount:.2f}")
print(f"Intrest earned in {time} is : ${intrest_earned:.2f}")

# the 2nd variation in 2:05:00 in bro code video yet to understand 
# i guess i understood 


#while True :
  #  time = float(input("Enter the Time (in years):"))
    #if time < 0 :
   #     print("Time cant be less than  0")
   # else :
    #    break

