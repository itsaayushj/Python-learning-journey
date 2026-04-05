#  Decorator  = A function that extends the behaviour of another function 
#               w/o modifying th ebase function 
#               Pass the base function as an argument to the decorator 


#               @add_sprinkles 
#               get_ice_cream("vanilla")


def add_sprinkles(function) : 
    def wrapper(*args) : #wrapper is created so it does not return until its called 
        print("^Sprinkles are added^")
        function(*args) 
    return wrapper

def add_dips(function) : 
    def wrapper(*args) : 
        print("^Your ice cream is dipped in chocolate^")
        function(*args)
    return wrapper


@add_dips
@add_sprinkles
def get_ice_cream(flavour) : 
    print(f"Here is your {flavour} ice cream🍧")

get_ice_cream("vanilla")
