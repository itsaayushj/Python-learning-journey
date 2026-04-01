class shapes : 
    def __init__(self , color , filled) : 
        self.color = color 
        self.filled = filled

    def shape_details(self) : 
        print(f"It is of {self.color} and {"filled" if self.filled else "not filled" }")

class circle(shapes) : 
    def __init__(self , color , filled , radius) : 
        super().__init__(color , filled )
        self.radius = radius 

    def shape_details(self) : # IT WILL OVERWRITE THE shape_details METHOD OF SHAPES
        print(f"it is of {self.color} color and is {"filled" if self.filled else "not filled" } and has a area of {3.14 * self.radius ** 2} cm  ")

circle1 = circle("red" , False , 5)

circle1.shape_details()
