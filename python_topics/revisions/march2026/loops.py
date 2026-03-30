# loops revision 
#while loop 
n = 0 
while True : 
    n += 1 
    
    if n == 10 :
        continue 
    else : 
        print(n)
    if n == 20 : 
        break

# for loop 
user_input_start = int(input("Enter the starting point : "))
user_input_end = int(input("Enter the ending point"))
skip_number_check = input("any number you hate and want to skip? Y for yes N for no  :  ").lower()

if skip_number_check == "n" : 
    for x in range(user_input_start , user_input_end + 1 ) : 

        print(x)
else : 
    skip_number = int(input("Enter the number you want to skip : "))
    for x in range(user_input_start , user_input_end + 1) : 
        if x == skip_number :
            continue 
        else : 
            print(x)
