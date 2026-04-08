
def repeater(number) : 
    def starter(function) : 
        def wrapper(*args) : 
            for num in range(number) : 
                result =function(*args)
            return result
        return wrapper
    return starter

@repeater(3)
def add(a , b) :
    return a+b 

print(add(3,4))

