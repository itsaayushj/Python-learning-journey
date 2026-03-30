import time 
input_time = int(input("Enter your time in seconds : "))
for x in reversed(range(1, input_time)): 
    seconds = x % 60 
    minutes = (x // 60) % 60 
    hours = x // 60 // 60 
    print(f"{hours :02} : {minutes :02} : {seconds :02}")
    time.sleep(1)