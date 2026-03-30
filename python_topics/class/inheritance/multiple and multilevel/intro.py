# multiple inheritance = inherit from more than one parent class 
#                          C(A,B)

# Multilevel inheritance = inherti from a parent which inhertis from another parent 
#                           C(B) <-B(A) <- A

# if there are two constructors (__init__) then the first one will be used unless its told to use both 
class animals : #grandparent class
    def __init__(self , name) : 
        self.name = name 

    def sleep(self) :
        print(f"{self.name} is sleeping !")

    def eat(self) : 
        print(f"{self.name} is eating!")

class hunters(animals) :  # parent channel 1
    def hunt(self):
        print(f"{self.name} is hunting😈")

class runners(animals) : # parent channel 2 
    def run(self):
        print(f"{self.name} is running 😥")

class sheeps(runners) :  # child class 
    pass
class lions(hunters) :      # child class
    pass
class cats(runners , hunters) :     # child class
    pass

sheep1 = sheeps("shawn")
lion1 = lions("simba")
cat1 = cats("garfield")

sheep1.eat()
sheep1.run()
lion1.hunt()
cat1.run()
cat1.hunt()
