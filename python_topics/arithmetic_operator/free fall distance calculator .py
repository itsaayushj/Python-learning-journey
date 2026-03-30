print("Welcome to free fall distance calculator")
t = float(input("Enter the time in seconds : "))
g = 9.8
distance_fallen = (1/2)*g *t**2
#distance_fallen = (1/2)*g pow(t, 2)
print(f"distance fallen : {round(distance_fallen , 2)}")
s = float(input("Enter  the distance fallen :"))  # this distance fallen is different... if we take same one the answer will be 0 
u = (s - 0.5 * g * t**2) / t
print(f"Initial velocity is : { round(u , 2)}")

# dont come here again i hate physics