#  static methods = a method that belongs to a class rather than any object from that class (instance) 
#                   usually used for general utility functions 
#  instance methods = best for operations on instance of the class (objects)
#  static methods = Best for utility functions that do not need access to class data

class Employee : 
    def __init__(self , name , position):
        self.name = name 
        self.position = position 

    def get_info(self) :# this is a instance method , every object created by this class will have its own instance method 
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_validposition(position) :  #it is a general utility method we dont need to create any object to use this we can directly use it.
        #static method dont use "self" like other method 
        valid_position = ["manager" , "cashier" , "cook" , "janitor"]
        return position in valid_position 

employee1 = Employee("Spongebob" , "cook")
employee2 = Employee("krabs" , "manager")
employee3 = Employee("patrick" , "clown")
print(Employee.is_validposition("cook"))
print(Employee.is_validposition("Teacher"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(Employee.is_validposition(employee1.position)) # works
print(Employee.is_validposition(employee2.position))
print(Employee.is_validposition(employee3.position))
print(employee1.is_validposition(employee1.position)) # it works too . we can also call a static method with object name. 
# Even if called using an object, static methods do NOT use instance (self) or class (cls).
# Best practice: call them using the class name.