# keyword arguments = an argument procedeed by a identifier
#                           Helps with readability 
#                       order of argument doesnt matter
#       1= positional argument 2 = Default argumetns 3 = keywords 4 = arbitary 

def greeting(greetings , title , first_name , last_name) : 
    print(f"{greetings} {title}{first_name.capitalize()} {last_name.capitalize()}")

greeting("hello" , last_name="jha" , first_name="aayush" , title="Mr.")



# extra    
print(1 , 2 , 3 , 4  , sep="X")


