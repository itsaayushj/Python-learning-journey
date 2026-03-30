# shipping adress 
def customer_details(*args , **kwargs) : 
    for arg in args : 
        print(arg.capitalize() , end = " ")
    print()
    if "apt" in kwargs :
        print(f"{kwargs.get('apt')} , {kwargs.get('road')} , {kwargs.get('pincode')}")
        if "mailbox" in kwargs : 
            print(f"{kwargs.get('apt')} , {kwargs.get('road')} , {kwargs.get('pincode')}")
            print(kwargs.get('mailbox'))
    else :
        print(f"{'road'} , {'pincode'}")
    print(f"{kwargs.get('city')} , {kwargs.get('state')} , {kwargs.get('country')}")
    print(f"Contact - {kwargs.get('phno')}")

customer_details("mr." ,  "aayush" , "jha" , apt = "44a" , road = "tollygunge road" , pincode = "700026" , city = "kolkata"  , state = "wb" , country = "India" )

    
