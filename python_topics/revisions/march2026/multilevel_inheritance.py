# multilevel inheritance revision 

# multiple inheritacne = c(a , b)
# multilevel inheritacne = c(b) <- b(a) <- a

class animals : 
    def __init__(self , name) : 
        self.name = name

    def eat(self) : 
        print(f"{self.name} eats!")

    def sleep(self) : 
        print(f"{self.name} sleeps!")

class hunter(animals)  :
    def hunt(self) : 
        print(f"{self.name} hunts!")

class runner(animals) : 
    def run(self) : 
        print(f"{self.name} runs!")

class tiger(hunter) : 
    def speak(self) : 
        print(f"{self.name} says roahhhh!")

class mouse(runner) : 
    def speak(self) : 
        print(f"{self.name} says chiii!")

class cat(hunter , runner) : 
    def speak(self) : 
        print(f"{self.name} says meow!")

tiger1 = tiger("winnie")
mouse1 = mouse("jerry")
cat1 = cat("tom")

tiger1.speak()
tiger1.hunt()
tiger1.sleep()


mouse1.speak()
mouse1.run()
mouse1.sleep()


cat1.speak()
cat1.hunt()
cat1.run()
cat1.sleep()
