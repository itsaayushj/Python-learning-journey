import datetime
current_datetime = datetime.datetime.now()
target_datetime = datetime.datetime(2026 , 9 , 19 , 12 , 4 , 33) #using year , month , day , hour , minute , second format     (Descending order)
print(f"Current date - {current_datetime}")
print(f"Target date - {target_datetime}")

if current_datetime < target_datetime : # python can check datetime
    print("The date has not passed yet!")
else : 
    print("The date has already passed!")

