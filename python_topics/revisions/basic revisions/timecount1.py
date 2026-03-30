import time 
user_input = int(input("Enter the time in seconds  :"))
for i in reversed(range(user_input + 1)) :
    seconds =  i % 60 
    minutes =  i // 60 % 60 
    hours = i // 3600 
    print(f"{hours:02d} : {minutes:02d} : {seconds:02d}")
    time.sleep(1)
    

