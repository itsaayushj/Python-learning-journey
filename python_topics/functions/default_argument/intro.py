# default arguments = a default value for certain parameters  . Default is used when tha targument is omitted . It makes the function more flexible. reduces # of arguments
# 1= positional argument 2 = Default argumetns 3 = keywords 4 = arbitary 
 
import time 


#eg 1 
#simple interest calculator 
def simple_int(principal , time = 1 , rate = 6) : 
    si = (principal * time * rate) / 100 
    # return (principal * time * rate) / 100 
    return si 

print(simple_int(100))

def counter(end , start = 0 ) : 
    for i in range(start , end+1 ) : 
        print(i)
        time.sleep(.5)
    print("done")

counter(10 , 0)