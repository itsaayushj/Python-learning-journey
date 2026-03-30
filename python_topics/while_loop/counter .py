number1 = int(input("Enter the number where you want the countdown to start:"))
number2 = int(input("Enter the number where you want cuntdown to end"))
print("the end number cant be smaller than start number" if number1 > number2 else "Lets do it!" )
if number1 < number2 :
    print(number1)
    while number1 != number2 :       
     number1 += 1
     print(number1)
# for this if i enter 1 count was starting from 2 but i wanted from 1 so i printed it once before the loop
#entered 1000000000000000000 as 2nd number and it kinda crashed lmao lagged (jk)
