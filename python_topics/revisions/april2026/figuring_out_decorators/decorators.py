def add_upper(function): 
    def wrapper(*args):
        print("Here is your uppercase alphabets")
        function(*args)
    return wrapper

def add_lower(function):
    def wrapper(*args):
        print("Here is your lowercase alphabets")
        function(*args)
    return wrapper

@add_upper
@add_lower
def alphabets():
    print("Here is your alphabets")



alphabets()
