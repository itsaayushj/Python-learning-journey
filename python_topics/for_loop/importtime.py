import time

input_time = int(input("Enter your time (in seconds) : "))
input_time += 1 
for x in reversed(range(1 , input_time)) :
    seconds = x % 60 
    minutes = int(x / 60) % 60 
    print(f"00:{minutes :02}:{seconds :02}")
    time.sleep(1)

print("Times Up!")
