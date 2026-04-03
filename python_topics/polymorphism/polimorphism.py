#  Polimorphism = Greek word that means to "have many form or face"
# poly = Many 
# morphe = Form 
# TWO WAY TO ACHEIVE POLIMORPHISM 
#  1- INHERITANCE - An object could be treated of the same type as a parent classs
#  "duck typing" = Object must have necessary attributes / methods

from abc import ABC , abstractmethod

class Shape(ABC) : #ABC doesnt allow shape to run directly . it can only be called in child class and not just by shape() (ABC works only when there is abstractmethod inside the class too. Otherwise we can call the class directl)
    @abstractmethod # it checks that all child class has area method in them 
    # abstractmethod applies only to the only one  method mentioned just below it 
    def area(self) :
        pass

class Circle(Shape) : 
    def __init__(self , radius) : 
        self.radius = radius

    def area(self) : 
        return 3.14 * self.radius **2 

class Square(Shape) : 
    def __init__(self , side) : 
        self.side = side
    
    def area(self) : 
        return self.side ** 2

class Triangle(Shape) : 
    def __init__(self , height , base) : 
        self.height = height
        self.base = base
    
    def area(self) : 
        return (self.height * self.base) / 2 


shapes = [Circle(4) , Square(5) , Triangle(6 ,7)]

for shape in shapes : 
    print(f"{shape.area()}cm² ") 