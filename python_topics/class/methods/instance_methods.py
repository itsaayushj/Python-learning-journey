# Instance methods = A method that works with a specific object (instance) of the class

# This is the normal and most common method we use with a class

class zoo :
    def __init__(self , name , species) : 
        self.name = name 
        self.species = species

    def about_it(self) : # this is a instance method as it works on a instance(object) It uses self parameters
        return f"The name of the animal is {self.name} and it is a {self.species}" 
    

animal1 = zoo("nemo" , "fish")
animal2 = zoo("poo" , "bear")

print(animal1.about_it()) # we call instance method with the help of Instance (object)
print(animal2.about_it())
