# super() = Function used in a child class to call method from  a parent class (superclass)
#               Allow you to extend the functionality of the inherited 
#               methods


    # child class = sub class
    # parent class = super calss 

# if a child and a parent have a method with the same name the child's method is taken 


# if there are two parent class and super() is called it will call both class's method
class shapes : 
    def __init__(self , color , filled) : 
        self.color = color 
        self.filled = filled
    def self_is(self) :
        print(f"It is  {self.color} and {'filled' if self.filled else 'Not filled'}") 

class circle(shapes) : 
    def __init__(self , color , filled , radius) : 
        # self.color = color 
        # self.filled = filled
        super().__init__(color , filled)
        self.radius = radius 
    
    def self_is(self):
        print(f"It has a area of {3.14 * self.radius ** 2  }")
        super().self_is()

class square(shapes) : 
    def __init__(self , color , filled , width) : 
        # self.color = color 
        # self.filled = filled
        super().__init__(color , filled)
        self.width = width

    def self_is(self):
        print(f"It has a area of {1/2 * self.width * self.width }")
        super().self_is()

class triange(shapes) : 
    def __init__(self , color , filled , width , height) : 
        # self.color = color 
        # self.filled = filled
        super().__init__(color , filled) 
        self.width = width 
        self.height = height
    def self_is(self) : 
        print(f"It has a area of {1/2 * self.width * self.height }")
        super().self_is()

circle1 = circle(color= "red" , filled=True , radius= 5)
print(circle1.color)
print(circle1.filled)
print(circle1.radius)
circle1.self_is()
square1 = square(color="blue" , filled = True , width= 10 )

print(square1.color)
print(square1.filled)
print(square1.width)
square1.self_is()


triangle1 = triange(color="pink" , filled = True , width= 10 , height=18 )

print(triangle1.color)
print(triangle1.filled)
print(f"{triangle1.width} cm")
print(f"{triangle1.height} cm")
triangle1.self_is() # we used a self_is method of triangle class (Child) and it overwrite the shapes class (parent) 
# method overwriting

# here super() = shapes
