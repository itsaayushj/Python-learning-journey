# format specifiers = {value:flags} format a value based on what flags are inserted 

price1 = 1499.999
price2 = 5000.250
price3 = 10000000
price4 = 250 
price5 = 1234567.98765
print(f"price 1 is ${price1:010}") # 10 is the total space it will take.... if space is less tham size of digit it will stay in its original size 010 means it adds 0 before blank space in front
print(f"price 2 is ${price2:.1f}") #.1f means 1 floating point decimal adding more will just add 0 as default 
print(f"price 3 is ${price3 :,}") # adds comma to thousand place  
print(f"price 4 is ${price4:^10}") # ^ < > are allignments  ^ is middle and other as it is
print(f"price 5 is $ {price5 :+^30,.3f}")  #.3f just rounds it off and not just cuts in middle thats why .988 and not .987   

price6 = 100 
price7 = -783
price8 = -9992
price9 = 8330

print(f"price 6 is {price6 :+}") # + adds a + sign before positive number 
print(f"price 7 is {price7 :+}") #negatice number remain unchanged
print(f"price 8 is {price8 : }") # a " " or a gap means if its positive it will have a gap and if negative as it is 
print(f"price 9 is {price9 : }") # same applied here 