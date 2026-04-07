def repeater(number):
    def start(function):
        def wrapper(*args):
            for i in range(number) : 
                print("starting")
                function(*args)
                print("ending")
        return wrapper
    return start
        

@repeater(2)
def greeting():
    print("Hello There!")

greeting()

