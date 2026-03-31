# revising basic inheritance

class animals : 
    def __init__(self,name) : 
        self.name = name 

    def eat(self) : 
        print(f"{self.name} eats!")

    def sleep(self) : 
        print(f"{self.name} sleeps!")
    
class dog(animals) : 
    def speak(self) : 
        print(f"{self.name} says woof!")
class cat(animals) : 
    def speak(self) : 
        print(f"{self.name} says meow!")
        
dog1 = dog("pluto")
cat1 = cat("garfield")

dog1.speak()
dog1.eat()
dog1.sleep()

cat1.speak()
cat1.eat()
cat1.sleep()