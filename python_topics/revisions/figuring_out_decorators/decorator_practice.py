# trying to understand decoders 
# practice code 

def check_me() : 
    print("I am running")

def add_uppercase(function):
    def wrapper(*args) : # this args will take the language and will pass it down to the lowercase 
        print("Uppercase letters are added!")
        function(*args) # this calls add_lowercase
        check_me()
    return wrapper
    
def add_lowercase(function) : 
    def wrapper(*args) : 
        print("Lowercase letters are added!")
        function(*args)
        check_me()
    return wrapper 

@add_uppercase # we are basically calling the functions 
@add_lowercase
def alphabets(language) : 
    print(f"Here is your {language} alphabets")

alphabets("English")

# alphabets("English")
#    ↓
# UPPERCASE wrapper
#    ↓
# LOWERCASE wrapper
#    ↓
# original function