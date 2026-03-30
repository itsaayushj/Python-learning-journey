# a one line shortcut for if - else statment
# print and assign one of the value based on the conditions
#       x if condition else Y

#x = 784287878475
#print("even" if x %2 == 0 else "odd")
#print(result)


a = float(input("Enter first number :"))
b = float(input("Enter the second number :"))
max_number = a if a > b else b 
min_number = a if a < b else b 
print(f"Maximum number is {max_number} and the minimum number is {min_number}")

