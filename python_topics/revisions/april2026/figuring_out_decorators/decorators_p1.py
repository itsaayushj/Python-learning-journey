def start(function):
    def wrapper(*args , **kwargs):
        print("Starting.....")
        if_any_output =  function(*args , **kwargs)
        print("Finished!")
        return if_any_output
    return wrapper

@start
def greeting(name):
    print(f"Hello {name}!")

greeting("user")

