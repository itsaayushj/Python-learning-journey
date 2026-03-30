#  variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in 

# here we will take function_2 for example 
from math import e # here the value of e will be built-in variable
def function_1() : 
    e = 100 # This is Enclosed variable for function_2 
    def function_2() : 
        e = 1 # this is Local variable
        print(e)
    function_2()

e = 99   # This is Global variable as it is outside of any function 

function_1()

