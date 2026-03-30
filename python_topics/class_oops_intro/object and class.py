#  object = A "bundle" of related attributes (variable) and methods (functions) 
# eg - phone , cup , book 
#  you need a "class" to create many object

# class = (blueprint) used to design the structure and layout of an object 
class car : 
    def __init__ (self , model) : 
        self.model = model 

    def drive(self) : 
        print(f"You are driving {self.model}")

car1 = car("BMW")
car1.drive()



