# Write a program that:
# Takes a number as input
# Uses match-case
# Prints:
# "Zero" → if number is 0
# "Small number" → if number is 1–10
# "Teen number" → if number is 11–19
# "Even big number" → if number is greater than 20 and even
# "Odd big number" → if number is greater than 20 and odd

def number_classifier(number) :
    match number : 
        case 0 :
            print("Zero") 
        case n if 0 < n <= 10 :
            print("Small number")
        case n if 11 <= n <= 20 : 
            print("Teen number")
        case n if n > 20 and n % 2 == 0 :
            print("Even big number")
        case n if n > 20 and n % 2 != 0 : 
            print("Odd big number")

number_classifier(21)