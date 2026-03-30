import time 
start_point = int(input("Enter the starting point : "))
end_point = int(input("Enter the ending point : "))
order = input("Do you want this to be in ascending order or descending order? Press A for ascending and D for descending : ").upper()
def ascending_count(start_point , end_point) : 
    for x in range(start_point , end_point + 1 ) : 
        print(x)
        time.sleep(1)

def descending_count(start_point , end_point) : 
    for x in range(end_point , start_point , -1 ) : 
        print(x)
        time.sleep(1)

if order == "A" : 
    ascending_count(start_point , end_point) 
else  :
    descending_count(start_point , end_point)
