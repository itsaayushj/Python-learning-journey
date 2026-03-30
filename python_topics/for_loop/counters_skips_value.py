print("Lets count ")
number1 = int(input("Enter the number where you want the countdown to start:"))
number2 = int(input("Enter the number where you want cuntdown to end"))
print("the end number cant be smaller than start number" if number1 > number2 else "Lets do it!" )
unlucky_number = int(input("Enter the unlucky number"))
if number1 < unlucky_number < number2 :
    for x in range (number1 , number2 +1) :
        if x == unlucky_number :
            continue
        else :
            print(x)
else :
    print("Unlucky number needs to be between first and last number")