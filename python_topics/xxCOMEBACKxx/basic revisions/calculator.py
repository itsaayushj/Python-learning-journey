print("Lets make a calculator")
int1 = float(input("Enter first number : "))
int2 = float(input("Enter second number : "))
operator = input(" Chose a operator  ( + - / *) :")
if operator == "/" :
    output = int1 / int2
    print(round(output , 2))
elif operator == "+" :
    output = int1 + int2
    print(round(output , 2))
elif operator == "-" :
    output = int1 - int2
    print(round(output , 2))
elif operator == "*" :
    output = int1 * int2
    print(round(output , 2))
else :
    print("Invalid operator")

