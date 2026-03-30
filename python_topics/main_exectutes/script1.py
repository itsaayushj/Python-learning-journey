
print(__name__)
def yippe() : 

    print("Hello there script 1 running as a import file ")

def direct_run() : 
    print("The script 1 is runing directly!")

match __name__ : 
    case  'script1' : 
        yippe()
    case '__main__' : 
        direct_run()
