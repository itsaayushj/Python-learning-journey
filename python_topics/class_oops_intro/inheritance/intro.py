#  Inheritance = Allow a class to inherit attributes and methods from 
#                                                       another class 
#               helps with code reusablity 
#               class Child(parent) // sub(super) 

class animal : 
    def __init__(self , name) : 
        self.name = name 
        self.is_alive = True 
    def walks(self) : 
        print(f"{self.name} is walking!") 
    def sleeps(self) : 
        print(f"{self.name} is sleeping!")
    
class dog(animal) : 
    def speaks(self) : 
        print(f"{self.name} says WOOF!")

class cat(animal) : 
    def speaks(self) : 
        print(f"{self.name} says MEOW!")


dog1 = dog("alex")
cat1 = cat("loofi")
print(dog1.name )
dog1.speaks()
dog1.sleeps()



