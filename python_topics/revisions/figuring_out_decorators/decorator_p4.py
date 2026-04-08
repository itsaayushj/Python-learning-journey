def counter(number):
    def starter(function) : 
        def wrapper(*args , **kwargs):
            for num in range(number) : 
                print("Start")
                result =function(*args , **kwargs)
            return result
        return wrapper
    return starter
    
@counter(2)
def main():
    print("Hello user!")


main()