def counter(number) :
    def starter(function) : 
        def wrapper(*args , **kwargs) : 
            print("start")
            function(*args , **kwargs)
            print("End")
            
        return wrapper
    return starter




@counter(4)
def add(a , b) : 
    print(a+b)

add(2 , 3)
