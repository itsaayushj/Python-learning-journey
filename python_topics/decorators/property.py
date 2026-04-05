#  @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#              Benefit: Add additional logic when read , write , or delete attributes
#              Gives you getter, setter and deleter method  

class Rectangle : 
    def __init__(self , width , height):
        self._width = width  #  _width is a "protected" attribute by convention (not truly private) we use _ before attribute to mark it as private but its not truly private 
        self._height = height 

    @property    # allows method to be accessed like an attribute (no parentheses)  
    def width(self) : 
        return f"{self._width:.1f} cm"
    @property 
    def height(self) : 
        return f"{self._height:.1f} cm"

    @width.setter           # to change a attribute 
    # setter allows controlled modification of the attribute
    def width(self , new_width) : 
        if new_width > 0 : 
            self._width = new_width
        else : 
            print("Invalid width")
    
    @height.setter 
    def height(self , new_height) : 
        if new_height > 0 : 
            self._height = new_height
        else : 
            print("Invalid height")
    
    @width.deleter          #to delete a attribute
    def width(self) : 
        del self._width
        print("Width has been deleted") # to check if its working
    
    @height.deleter
    def height(self) : 
        del self._height
        print("Height has been deleted") # to check if its working 

# we cannot do this because if we do it in this method then we have to call width by width() so we use #width.getter so we can call it like a atrribute and not as a function
    # def width(self):
    #     return f"{self.width:1f} cm"        
    # def outputs_height(self) : 
    #     return f"{self.height:1f} cm"
    # without @property, width would be a method and require width()
# @property lets us access it like an attribute instead

rectangle1 = Rectangle(10 ,20)

print(rectangle1.width , rectangle1.height)  # to check if @property is working

rectangle1.height = 4 
rectangle1.width = 5
print(rectangle1.width , rectangle1.height) # to check if @setter is working

del rectangle1.height
del rectangle1.width
# print(rectangle1.width , rectangle1.height)   This will show error because there are no more attributes 