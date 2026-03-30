#  Polimorphism = Greek word that means to "have many form or face"
# poly = Many 
# morphe = Form 
# TWO WAY TO ACHEIVE POLIMORPHISM 
#  1- INHERITANCE - An object could be treated of the same type as a parent classs
#  "duck typing" = Object must have necessary attributes / methods

class shape : 
    
    def area(self) : 
        pass



class circle(shape) : 
    def __init__(self , radius) : 
        self.radius = radius
    def area(self) : 
        return 3.14 * self.radius ** 2 

class square(shape) :
    def __init__(self , side) : 
        self.side = side 
    def area(self) : 
        return self.side ** 2 

class triange(shape) :
    def __init__(self,height , base) : 
        self.height = height
        self.width = base
    def area(self) : 
        return 1/2 
