import math
print("Lets calculate circumference")
r = float(input("Enter the radius:"))
circumference = r * math.pi * 2
print(f"circumference of the circle with radius of {r}cm is {round(circumference, 2)}") # ,2 is for rounding it to 2 digits after decimal
#works fine...can we find a more fast way?
#circumference = print( r * math.pi * 2)
#i mean yeah but the 2 line one is more beauiful i guess