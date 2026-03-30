def hbd(name , age ) : 
    print(f"Happpy birthday {name} , You are {age} years old now!")

hbd("aayush", 19)

def invoice(name , amount , date) : 
    print(f"Hello {name} , your total bill is of ${amount} your due date is {date}")

invoice("aayush",100 , "19 March")

def add (a , b) : 
    c = a + b 
    return c 


print(add(10 , 20 ))



def fullname(first , last):
    return first.capitalize() + " " + last.capitalize()

print(fullname("aayush" , "jha"))

import time
def count(end , start = 0 ): 
    for x in range(start , end +1) : 
        print(x)
        time.sleep(0.5)
    print("Done")
count( 10 )

def hello(greeting ,  first_name , last_name , title = "Mr" ) :
    print(f"{greeting} {title} {first_name} {last_name} ")

hello("hello" , last_name="jha" , first_name= "aayush" )


