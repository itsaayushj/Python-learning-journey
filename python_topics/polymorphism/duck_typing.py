#  duck typing = another way to achieve polymorphism besides inheritance
#                   object must have the minimum necessary attributes / methods
#               "if it looks like a duck and quack like a duck , it must be a duck"

class Animals : 
    alive = True 

class Dog(Animals) : 
    def speak(self) : 
        print("woof!")

class Cat(Animals) :
    def speak(self) : 
        print("meow!")

class car :
    alive = True
    def speak(self) : 
        print("honk!")

animals = [Dog() , Cat() , car()]
# here python does not care if car inherits from same super class or not. It will run if the OBJECT has the necessary methods/attributes when used otherwise it will give error 
for animal in animals : 
    animal.speak()
    print(animal.alive)


