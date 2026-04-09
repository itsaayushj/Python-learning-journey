# exception = An event that interrupts the flow of a program 
#       (ZeroDivisionError , TypeError , ValueError and many more)
#       1.try , 2.except , 3.finally

try :
    number = int(input("Enter a Number! : "))
    1 / number
# except Exception :  # covers all the excepion 
#     print("Something went wrong ")
except ZeroDivisionError : 
    print("Cant divide with zero!")
except ValueError : 
    print("Only numbers are allowed")
finally : # finally will always run no matter if its try or except
    print("Wrap it up!")
    