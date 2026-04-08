
def starter(function) :
    def wrapper(*args , **kwargs) :  
        print("Start")
        result_ifany = function(*args , **kwargs)
        print("End")
        return result_ifany
    return wrapper

@starter
def main(name): 
    print(f"Hello {name}!")

main("user")

