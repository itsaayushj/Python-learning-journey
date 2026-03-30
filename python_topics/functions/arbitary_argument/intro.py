#  *args = allow you to pass multiple non-key arguments / returns tuple
#  **kwargs = allow you to pass multiple keyword-arguments  / returns dictionary 
#               * unpacking operator
#   1 = positional 2 = default 3 = keyword 4 = arbitary 


#  args--------------------
def add(*args) : 
    total = 0 
    for arg in args :
        total += arg 
    return total 

print(add(100 , 200 ,400 , 500 , 600 , 700 , 800 , 900 , 1000))

def namer(*name_parts) : 
    for name in name_parts : 
        print(f"{name.capitalize()}" , end = " ")

print(namer("aa", "bb" , "cc" , ))

#  kwargs--------------------
def adress_namer(**kwargs):
    for key , value in kwargs.items() : 
        print(f"{key.capitalize()} : {value.capitalize()}" , end = " ; ")

adress_namer(country = "India" , state = "Delhi" , city = "New delhi" , street = "123 , Fake street" , apartment_number = "1B" , pincode = "91" )





