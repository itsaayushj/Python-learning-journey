import math
print("Lets calculate hypotenous of a right angle triangle")
a = float(input("Enter side a of the triangle"))
b = float(input("Enter side b of the triangle"))
#c = math.sqrt(math.pow(a , 2) + math.pow(b , 2))
c = math.sqrt(a **2 + b **2 )
print(f"hypotenuse of triangle is {round(c , 2)}")
