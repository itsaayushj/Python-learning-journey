print("Welcome to a beginners calculator")
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
output = 0
operator = input("Enter the operator you want( + , - , * , / )")
if operator == "+" :
    output = num1 + num2
    print(round(output , 2))
elif operator == "-":
    output = num1 - num2
    print(round(output , 2))
elif operator == "*":
    output = num1 * num2 
    print(round(output , 2))

elif operator == "/":
    output = num1 / num2
    print(round(output , 2))
else :
    print("Invalid operator or operator is not supported in this program")
print("I hope you never visit again ")
