def add(*args) :
    x = 0 
    for arg in args : 
        x += arg
    return x 

total = add(10 , 20 , 29 , 894, 893 )

print(total )

def shipping_label(*args , **kwargs) : 
    for arg in args : 
        print (str(arg).capitalize() , end = " ")
    if "apt" in kwargs : 
        print(kwargs.get('apt') , kwargs.get('street') , kwargs.get('pincode'))
    else : 
        print(kwargs.get('street') , kwargs.get('pincode'))
    print(kwargs.get('city') , kwargs.get('state'))

shipping_label("Mr." , "bruce" , "wayne" ,
               apt = "1A" , street = "wayne street" , pincode = 6969 , city = "gotham" , state = "New jersey")


