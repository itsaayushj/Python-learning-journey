# Membership operator = used  to test whether a value or variable is found  in a sequence 
#                           (string , list , tuple , set or dictionary )
#                               1. in 
#                              2 . not in 

aayush = "aayush"
if "a" in aayush : 
    print("Yes")

list = [0, 1, 2, 3, 4, 5, 6, 7]
if 8 in list : 
    print("Yes")
if 11 in list : 
    print("Yes")
else : 
    print("No")

dictionary = { "a" : 1}
x = "a"
if x in dictionary : 
    print(dictionary.get(x))
    
