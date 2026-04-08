
def starter(function): 
    def wrapper(*args , **kwargs):
        print("Start")
        result = function(*args , **kwargs)
        print("End")
        return result    
    return wrapper
@starter
def add(a , b) : 
    return a + b

print(add(2 , 3))
